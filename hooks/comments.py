"""Inject the Utterances comment thread on every blog page.

Comments are stored as GitHub issues in onyxgod777/pi (the repo the Utterances
app is installed on), matched by issue-term=pathname, so each page owns exactly
one thread and old threads stay attached as long as the URL does not change.

A hook is used instead of a theme override so the block survives mkdocs-material
upgrades, and blog/ is filtered explicitly because only posts carry threads.
"""

COMMENTS_BLOCK = """
<div class="comments-section" id="comments">
  <h3>💬 Leave a Comment</h3>
  <p class="comments-note">
    Sign in with GitHub to join the thread. Comments are stored as issues in
    <a href="https://github.com/onyxgod777/pi/issues" target="_blank" rel="noopener">onyxgod777/pi</a>
    and appear here automatically.
  </p>
  <script src="https://utteranc.es/client.js"
    repo="onyxgod777/pi"
    issue-term="pathname"
    label="💬 comment"
    theme="github-dark"
    crossorigin="anonymous"
    async>
  </script>
</div>
"""


def on_page_content(html, page, config, files):
    url = page.url or ""
    if url.startswith("blog/"):
        return html + COMMENTS_BLOCK
    return html
