#!/usr/bin/env python3
"""Generate static redirect .html files so old post URLs (/blog/posts/NAME.html)
redirect to the new MkDocs pretty URLs (/blog/posts/NAME/)."""
import glob
import os

POSTS = sorted(glob.glob('docs/blog/posts/*.md'))

TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<link rel="canonical" href="https://pi.thealpha-secret.xyz/blog/posts/{name}/">
<meta http-equiv="refresh" content="0; url=/blog/posts/{name}/">
<script>location.replace("/blog/posts/{name}/");</script>
<title>Redirecting…</title>
</head>
<body>
<a href="/blog/posts/{name}/">This article has moved. Click here to continue.</a>
</body>
</html>
"""

count = 0
for f in POSTS:
    name = os.path.basename(f)[:-3]
    out = os.path.join('docs/blog/posts', name + '.html')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(TMPL.format(name=name))
    count += 1

print(f"generated {count} redirect .html files")
