#!/usr/bin/env python3
"""Convert standalone HTML blog posts in docs/blog/posts/ to uniform markdown
for MkDocs Material rendering.

Strategy:
  * Locate the content root (<main> / <article> / content .container / <body>).
  * Strip site chrome: header, footer, nav, comments, social, support, back-link,
    share, brand/cta, resource/cross links, scripts, styles, forms, canvases.
  * Convert styled content boxes (proof-box, highlight-box, callout, equation,
    etc.) to markdown blockquotes so they render uniformly in Material.
  * Emit YAML frontmatter (title, date, description) + article body.
  * Rewrite internal .html links to MkDocs pretty URLs (trailing slash).
"""
import glob
import os
import re
import sys
from bs4 import BeautifulSoup
import markdownify

POSTS = sorted(glob.glob('docs/blog/posts/*.html'))
OUT = 'docs/blog/posts'  # markdown files land here alongside; html deleted later

CHROME_SELECTORS = [
    'header', 'footer', 'nav', 'script', 'style', 'noscript', 'iframe', 'form',
    'canvas', 'svg',
    '.comments-section', '.social-bar', '.social', '.share', '.support-section',
    '.support-buttons', '.support-btn', '.back-link', '.brand-cta', '.cta-soft',
    '.cta-box', '.resource-links', '.nav-links', '.menu', '.hamburger',
    '.toggle-switch', '.toggle-slider', '.toggle-label', '.toggle',
    '.error-card', '.error-msg', '.error-bar-track', '.error-bar-container',
    '.cross-links', '.meta-pagination', '.pagination', '.post-navigation',
    '.category-card', '.domain-card',
]

BOX_SUBSTR = (
    'box', 'callout', 'note', 'quote', 'refutation', 'theorem', 'verdict',
    'result', 'summary', 'equation', 'formula', 'highlight', 'proof',
    'refutation', 'statement', 'stance',
)

DATE_RE = re.compile(
    r'(?:published\s*)?'
    r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*'
    r'\s+\d{1,2},?\s+\d{4}',
    re.IGNORECASE,
)
# 2026-07-31 style
ISO_RE = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')


def classes(el):
    if el is None:
        return set()
    return set(el.get('class') or [])


def is_chrome(el):
    if el is None or getattr(el, 'parent', None) is None:
        return False
    if el.name in ('header', 'footer', 'nav', 'script', 'style', 'noscript',
                   'iframe', 'form', 'canvas', 'svg'):
        return True
    for c in classes(el):
        cl = c.lower()
        if any(sel in cl for sel in (
                'comments-section', 'social-bar', 'support', 'back-link',
                'brand-cta', 'cta', 'resource-links', 'nav-links', 'hamburger',
                'menu', 'toggle', 'share', 'pagination', 'post-navigation',
                'category-card', 'domain-card', 'error-card', 'error-msg')):
            return True
    return False


def is_box(el):
    if el.name not in ('div', 'section', 'blockquote'):
        return False
    return any(any(b in c for b in BOX_SUBSTR) for c in classes(el))


def find_content_root(soup):
    # remove chrome first
    for el in list(soup.select('header,footer,nav,script,style,noscript,iframe,form,canvas,svg')):
        el.decompose()
    for el in soup.find_all(True):
        if is_chrome(el):
            el.decompose()

    body = soup.body or soup
    if body.find('main'):
        return body.find('main')
    if body.find('article'):
        return body.find('article')
    # content .container: the last/first container that still has substantial text
    for c in body.find_all('div'):
        if 'container' in classes(c) and c.parent is not None:
            txt = c.get_text(' ', strip=True)
            if len(txt) > 200:
                return c
    return body


def extract_meta(soup, content):
    # title
    h1 = content.find('h1')
    title = h1.get_text(strip=True) if h1 else None
    if not title:
        t = soup.find('title')
        if t:
            title = re.sub(r'\s*[—|–-]\s*The True Value Of Pi.*$', '', t.get_text(strip=True))
    # description
    desc = None
    m = soup.find('meta', attrs={'name': 'description'})
    if m and m.get('content'):
        desc = m['content'].strip()
    # date
    date = None
    date_el = None
    # 1) dedicated date elements
    for el in content.find_all(['div', 'p', 'span', 'time']):
        cls = classes(el)
        if any(any(d in c for d in ('date', 'post-meta', 'meta', 'published', 'timestamp')) for c in cls):
            t = el.get_text(' ', strip=True)
            mm = ISO_RE.search(t) or DATE_RE.search(t)
            if mm:
                date = mm.group(0)
                date_el = el
                break
    if not date:
        # 2) scan first paragraphs for a "Published ..." line
        for el in content.find_all('p')[:6]:
            t = el.get_text(' ', strip=True)
            if DATE_RE.search(t) and len(t) < 80:
                mm = DATE_RE.search(t)
                date = mm.group(0)
                date_el = el
                break
    return title, date, desc, h1, date_el


def normalize_date(d):
    if not d:
        return None
    m = ISO_RE.search(d)
    if m:
        return m.group(0)
    months = {mo: i + 1 for i, mo in enumerate(
        ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
         'oct', 'nov', 'dec'])}
    pat = r'\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b'
    mo = re.search(pat, d, re.IGNORECASE)
    if mo:
        mon, day, year = mo.groups()
        return f"{year}-{months[mon.lower()]:02d}-{int(day):02d}"
    pat2 = r'\b(\d{1,2})(?:st|nd|rd|th)?\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{4})\b'
    mo2 = re.search(pat2, d, re.IGNORECASE)
    if mo2:
        day, mon, year = mo2.groups()
        return f"{year}-{months[mon.lower()]:02d}-{int(day):02d}"
    return None


def strip_title_date(content, h1, date_el):
    if h1:
        h1.decompose()
    if date_el and date_el is not h1:
        date_el.decompose()
    # remove any standalone "Published <date>" paragraphs and footer chrome lines
    for p in content.find_all('p'):
        t = p.get_text(' ', strip=True)
        low = t.lower()
        if re.fullmatch(r'published\s+.*\d{4}', t, re.IGNORECASE):
            p.decompose()
        elif 'read more on the golden pi wiki' in low or 'read more' in low:
            p.decompose()
    # remove lone horizontal-rules / empty divs that were page separators
    for hr in content.find_all('hr'):
        hr.decompose()


def box_to_blockquote(content):
    """Flatten styled content boxes (proof-box, callout, equation, etc.) so the
    article reads as clean uniform markdown. The box is only a visual wrapper in
    the old standalone pages; unwrapping promotes its children (headings,
    paragraphs, lists) to normal flow. Nested boxes are handled by re-scanning
    until stable."""
    for _ in range(3):
        hit = False
        for el in list(content.find_all(['div', 'section'])):
            if el.parent is None:
                continue
            if is_box(el):
                el.unwrap()
                hit = True
        if not hit:
            break


def convert(content):
    return markdownify.markdownify(
        str(content),
        heading_style='ATX',
        bullets='-',
        strong_em_symbol='*',
    )


def fix_links(md, post_names):
    def repl(m):
        prefix, target, suffix = m.group(1), m.group(2), m.group(3)
        t = target.strip()
        if not t.endswith('.html'):
            return m.group(0)
        base = t.split('/')[-1][:-5]
        if base in post_names:
            newt = f"/blog/posts/{base}/"
        elif base == 'calculator':
            newt = "/calculator/"
        elif base == 'index':
            newt = "/blog/"
        else:
            newt = '/' + t.lstrip('./').rsplit('/', 1)[-1][:-5] + '/'
        return f"{prefix}{newt}{suffix}"

    md = re.sub(r'(\[[^\]]*\]\()([^)]*?\.html)(\))', repl, md)
    # drop stray "back to blog" footer lines
    out = []
    for ln in md.split('\n'):
        if re.search(r'back to blog', ln, re.IGNORECASE) or '← Back' in ln:
            continue
        out.append(ln)
    return '\n'.join(out)


def clean_md(md):
    lines = md.split('\n')
    out = []
    blank = 0
    for ln in lines:
        s = ln.rstrip()
        if not s.strip():
            blank += 1
            if blank <= 1:
                out.append('')
            continue
        blank = 0
        out.append(s)
    md = '\n'.join(out).strip()
    return md


def main():
    report = []
    post_names = {os.path.basename(p)[:-5] for p in POSTS}
    for f in POSTS:
        name = os.path.basename(f)[:-5]  # strip .html
        with open(f, encoding='utf-8') as fh:
            html = fh.read()
        soup = BeautifulSoup(html, 'html.parser')
        content = find_content_root(soup)
        title, date, desc, h1, date_el = extract_meta(soup, content)
        strip_title_date(content, h1, date_el)
        box_to_blockquote(content)
        md = convert(content)
        md = fix_links(md, post_names)
        md = clean_md(md)

        norm_date = normalize_date(date)
        if not norm_date:
            norm_date = normalize_date(title or '')
        front = ['---']
        front.append(f'title: "{title}"' if title else 'title: ""')
        front.append(f'date: {norm_date}' if norm_date else 'date: ""')
        if desc:
            desc_one = ' '.join(desc.split())
            front.append(f'description: "{desc_one}"')
        front.append('---')
        body = f"\n\n{md}\n" if md else "\n"
        out_md = '\n'.join(front) + body

        out_path = os.path.join(OUT, name + '.md')
        with open(out_path, 'w', encoding='utf-8') as fh:
            fh.write(out_md)

        report.append((name, title, norm_date, len(md)))

    print(f"Converted {len(report)} posts to {OUT}/")
    for name, title, date, ln in report:
        t = (title or '')[:60]
        print(f"  {name} | date={date} | {ln}ch | {t}")


if __name__ == '__main__':
    main()
