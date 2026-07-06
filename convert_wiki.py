#!/usr/bin/env python3
"""Convert MkDocs Material compiled HTML to clean Markdown.
Rewrites link paths from old wiki/ subdirectory to new root docs/ structure."""

import re, os, html

REPO = "/home/kali/tvop.github.io"
OUT = "/home/kali/pi-wiki/docs"

PAGES = [
    # (output_md_path, source_html_path, section_depth_adjustment)
    # section_depth = how many ../ to strip from relative links
    ("index.md",                 "wiki/index.html", 0),
    ("golden-pi/true-value.md",  "wiki/golden-pi/true-value/index.html", 1),
    ("golden-pi/kepler-triangle.md", "wiki/golden-pi/kepler-triangle/index.html", 1),
    ("golden-pi/squaring-circle.md", "wiki/golden-pi/squaring-circle/index.html", 1),
    ("golden-ratio/phi.md",          "wiki/golden-ratio/phi/index.html", 1),
    ("golden-ratio/in-nature.md",    "wiki/golden-ratio/in-nature/index.html", 1),
    ("golden-ratio/in-architecture.md", "wiki/golden-ratio/in-architecture/index.html", 1),
    ("evidence/pyramid-of-giza.md",    "wiki/evidence/pyramid-of-giza/index.html", 1),
    ("evidence/ancient-knowledge.md",  "wiki/evidence/ancient-knowledge/index.html", 1),
    ("evidence/billy-meier.md",        "wiki/evidence/billy-meier/index.html", 1),
    ("resources/bibliography.md",      "wiki/resources/bibliography/index.html", 1),
    ("manual/squaring-the-circle.md",  "wiki/manual/squaring-the-circle.html", 1),
    ("manual/true-value-of-pi.md",     "wiki/manual/true-value-of-pi.html", 1),
]

def fix_links(content, depth):
    """Rewrite relative wiki links for new file location.
    depth=1 means file is in a subdirectory (e.g. golden-pi/true-value.md).
    Old links: ../../golden-ratio/phi/ -> strip one ../ -> ../golden-ratio/phi/
    Old links: ../kepler-triangle/ -> no adjustment needed -> kepler-triangle/
    """
    def _fix(m):
        url = m.group(1)
        # Only fix relative links
        if url.startswith('../') or url.startswith('./') or not url.startswith(('http:', 'https:', '#', 'mailto:')):
            # Strip trailing /
            url_clean = url.rstrip('/')
            # Old links from wiki subdir had extra ../ sections we need to fix
            if depth == 1:
                # File is in docs/section/file.md, old link from wiki/section/page/index.html
                # Old: ../../golden-ratio/phi/ -> ../golden-ratio/phi/
                # Old: ../kepler-triangle/ -> kepler-triangle/
                # Old: ../../golden-pi/true-value/ -> ../golden-pi/true-value/
                parts = url_clean.split('/')
                # Count how many .. we can remove
                while len(parts) > 1 and parts[0] == '..':
                    parts.pop(0)
                    break  # Remove just one level
                url_clean = '/'.join(parts)
            
            return m.group(0).replace(m.group(1), url_clean.rstrip('/'))
        return m.group(0)
    
    # Fix links in markdown
    content = re.sub(r'(?<=\]\()([^)]+)(?=\))', _fix, content)
    return content

def html_to_md(html_text, depth):
    """Extract and convert article content to Markdown."""
    # Find article area
    start = html_text.find('<article class="md-content__inner md-typeset">')
    if start == -1:
        start = html_text.find('<article')
        if start == -1:
            return None, None
    end = html_text.find('</article>', start)
    if end == -1:
        return None, None
    
    content = html_text[start:end]
    
    # Extract title
    title_match = re.search(r'<title>(.*?) - Golden Pi Wiki</title>', html_text)
    title = title_match.group(1) if title_match else None
    
    # Remove script/style tags and their content
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    
    # Remove header anchors (¶ links)
    content = re.sub(r'<a\s+class="md-header-anchor"[^>]*>.*?</a>', '', content)
    content = re.sub(r'<a\s+class="headerlink"[^>]*>.*?</a>', '', content)
    
    # Remove edit button
    content = re.sub(r'<a\s+class="md-content__button"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
    
    # Convert headers: h1 -> #
    content = re.sub(r'<h1[^>]*id="([^"]*)"[^>]*>(.*?)</h1>', r'# \2', content)
    content = re.sub(r'<h2[^>]*id="([^"]*)"[^>]*>(.*?)</h2>', r'## \2', content)
    content = re.sub(r'<h3[^>]*id="([^"]*)"[^>]*>(.*?)</h3>', r'### \2', content)
    content = re.sub(r'<h4[^>]*id="([^"]*)"[^>]*>(.*?)</h4>', r'#### \2', content)
    content = re.sub(r'<h5[^>]*id="([^"]*)"[^>]*>(.*?)</h5>', r'##### \2', content)
    
    # Catch headers without id attribute too
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content)
    
    # Convert tables to Markdown
    def _table_to_md(table_html):
        rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)
        md_rows = []
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            md_cells = []
            for c in cells:
                c = re.sub(r'<[^>]+>', '', c)
                c = html.unescape(c).strip()
                md_cells.append(c)
            md_rows.append('| ' + ' | '.join(md_cells) + ' |')
            if i == 0:
                # Header separator
                md_rows.append('|' + '|'.join([' --- '] * len(md_cells)) + '|')
        return '\n'.join(md_rows)
    
    content = re.sub(r'<table[^>]*>(.*?)</table>', lambda m: _table_to_md(m.group(0)), content, flags=re.DOTALL)
    
    # Convert <pre><code> blocks
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content)
    
    # Convert math: <p>$$...$$</p> -> $$...$$
    content = re.sub(r'<p>\s*\$\$(.*?)\$\$\s*</p>', r'$$\1$$', content, flags=re.DOTALL)
    # Convert inline math
    content = re.sub(r'<p>\s*\$(.*?)\$\s*</p>', r'$\1$', content, flags=re.DOTALL)
    
    # Convert paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Convert lists
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    content = re.sub(r'</?u[lol][^>]*>', '', content)
    
    # Convert images
    def _fix_img(m):
        src = m.group(1)
        alt = m.group(2) if m.group(2) else ''
        # Fix relative image paths from old wiki
        if not src.startswith(('http:', 'https:', 'data:')):
            # Strip leading ../../ pattern from old wiki references
            src = re.sub(r'^(\.\./)+', '', src)
            if depth > 0:
                src = '../' * depth + src
        return f'![{alt}]({src})'
    
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>', _fix_img, content)
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', lambda m: f'![]({m.group(1)})', content)
    
    # Convert links - handle both markdown-style and HTML
    def _link_fix(m):
        text = m.group(1).strip()
        url = m.group(2).strip()
        # Clean up HTML entities in URL
        url = url.replace('&amp;', '&')
        return f'[{text}]({url})'
    
    content = re.sub(r'<a\s+[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: f'[{m.group(2).strip()}]({m.group(1).strip()})', content, flags=re.DOTALL)
    
    # Bold/italic
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    
    # Horizontal rules
    content = re.sub(r'<hr[^>]*>', '\n---\n', content)
    
    # Blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1', content, flags=re.DOTALL)
    
    # Remove leftover HTML tags (div, span, br, etc.)
    content = re.sub(r'</?div[^>]*>', '', content)
    content = re.sub(r'</?span[^>]*>', '', content)
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Clean up
    content = re.sub(r'\n{4,}', '\n\n', content)
    content = content.strip()
    
    # Remove article tags
    content = re.sub(r'</?article[^>]*>', '', content)
    
    # Fix links in the generated markdown
    content = fix_links(content, depth)
    
    return content, title


for out_path, src_path, depth in PAGES:
    full_src = os.path.join(REPO, src_path)
    full_out = os.path.join(OUT, out_path)
    
    if not os.path.exists(full_src):
        print(f"MISSING: {full_src}")
        continue
    
    with open(full_src) as f:
        html_text = f.read()
    
    result = html_to_md(html_text, depth)
    if result is None:
        print(f"FAIL: {full_src}")
        continue
    
    content, title = result
    
    # Remove duplicate first H1 (the content already has one from the HTML)
    lines = content.split('\n')
    while lines and not lines[0].strip():
        lines.pop(0)
    
    os.makedirs(os.path.dirname(full_out), exist_ok=True)
    with open(full_out, 'w') as f:
        f.write(content + '\n')
    
    print(f"OK: {out_path} ({len(content)} chars, depth={depth})")
