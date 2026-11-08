"""Inject the Remark42 comment thread on every blog page.

Comments are served by a self-hosted Remark42 instance at
https://comments.thealpha-secret.xyz (site_id=pi). Each page's thread is keyed
by its URL, so threads persist as long as the URL does not change.

A hook is used instead of a theme override so the block survives mkdocs-material
upgrades, and blog/ is filtered explicitly because only posts carry threads.
"""

COMMENTS_BLOCK = """
<div class="comments-section" id="comments">
  <h3>💬 Comments</h3>
  <div id="remark42"></div>
  <script>
    var remark_config = {
      host: "https://comments.thealpha-secret.xyz",
      site_id: "pi",
      components: ["embed"],
      theme: "dark",
      max_shown_comments: 20
    };
  </script>
  <script>!function(e,n){for(var o=0;o<e.length;o++){var r=n.createElement("script"),c=".js",d=n.head||n.body;"noModule"in r?(r.type="module",c=".mjs"):r.async=!0;r.defer=!0;r.src=remark_config.host+"/web/"+e[o]+c;d.appendChild(r)}}(remark_config.components||["embed"],document);</script>
</div>
"""


def on_page_content(html, page, config, files):
    url = page.url or ""
    if url.startswith("blog/"):
        return html + COMMENTS_BLOCK
    return html
