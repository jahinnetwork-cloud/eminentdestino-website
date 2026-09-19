# Eminent Destino (EDO) website

Static multi-page site, deployed by Cloudflare Pages straight from this repo (no build step on Cloudflare).

## How it is organised
- `src/services.json`  Text of the 9 service pages, English (`en`) and Burmese (`my`). One source for tiles, pages, footer and the contact form.
- `src/site.js`        All behaviour: EN/Burmese switch (the `MY` object holds Burmese for the static text), hero video loader, logo loader, contact form, API sample.
- `src/style.css`      All styling. Orange #FF6B00 and white. Fully responsive.
- `build.py`           Generates `index.html` and `services/*.html` (each file is self-contained: CSS and JS are inlined).

## Rules
1. Edit `src/` and then run `python3 build.py`. Never hand-edit the generated HTML.
2. Commit the regenerated HTML together with the source change.
3. Every visible string needs an English version and a Burmese version (`data-i18n` key + entry in `MY` in `src/site.js`, or `en`/`my` in `services.json`).
4. Keep every file under 25 MiB (Cloudflare Pages limit). The hero video goes in `assets/hero.mp4` (H.264, aim for 8-15 MB), the logo in `assets/logo.png`.
5. Contact email is `info@eminentdestino.com` (`CONTACT_EMAIL` in `src/site.js`).
6. Do not promise results the company cannot guarantee (AdSense approval, revenue). Keep wording such as "help with" and "competitive".
