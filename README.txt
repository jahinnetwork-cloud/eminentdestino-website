EMINENT DESTINO WEBSITE
=======================
index.html              Home page            (generated)
services/*.html         9 service pages      (generated)
assets/                 Put logo.png and hero.mp4 here (see assets/README.txt)
src/                    SOURCE: services.json (service text EN+Burmese), style.css, site.js
build.py                Regenerates index.html and services/*.html from src/
CLAUDE.md               Instructions for Claude Code
_headers                Cloudflare Pages cache and security headers
.gitignore              Keeps junk files out of Git

EDIT THE SITE
-------------
Edit files in src/ (never edit the generated HTML by hand), then run:   python3 build.py
Commit everything, including the regenerated HTML. Cloudflare only serves the committed files.

Every page is self-contained (styles and scripts are inside the file). No build step.

DEPLOY: GITHUB + CLOUDFLARE PAGES
---------------------------------
1) Put the files of this folder in the ROOT of a GitHub repository
   (index.html must sit at the top level of the repo, not inside a sub-folder).
2) Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git > pick the repo.
3) Build settings:
     Framework preset ........ None
     Build command ........... (leave empty)
     Build output directory .. /        (a single slash, or leave the default)
4) Save and Deploy. Every git push to the main branch redeploys automatically.
5) Custom domain: Pages project > Custom domains > Set up a domain > eminentdestino.com

LIMITS
  Cloudflare Pages: max 25 MiB per file  ->  keep assets/hero.mp4 under 25 MB (aim for 8-15 MB).
  GitHub: max 100 MB per file (warning above 50 MB).

Contact form opens the visitor's email app addressed to info@eminentdestino.com.
Language switch (EN / Burmese) is in the top bar and is remembered.
