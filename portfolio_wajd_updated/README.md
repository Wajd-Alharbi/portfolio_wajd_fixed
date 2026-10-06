# Wajd Mazen Alharbi — Portfolio

Personal portfolio of **Wajd Mazen Alharbi**, AI Engineer (Automation & Agentic AI).
Single-page, bilingual (English / العربية, full RTL), light/dark theme, responsive.

The site is built from Python: `content.py` holds all text, `components.py` turns it
into semantic HTML, and `static/style.css` is the design system. The same markup is
served two ways:

| | Command | Use it for |
|---|---|---|
| **Streamlit app** | `streamlit run app.py` | Local preview / Streamlit Community Cloud |
| **Static site** | `python build.py` → `dist/` | Production hosting with full SEO (GitHub Pages, Netlify, Vercel) |

## Run locally

```bash
cd portfolio_wajd_updated
pip install -r requirements.txt
streamlit run app.py          # http://localhost:8501  (Arabic: ?lang=ar)
```

## Build the static site

```bash
python build.py               # no extra dependencies
python -m http.server -d dist # preview at http://localhost:8000
```

`dist/index.html` (English) and `dist/ar/index.html` (Arabic) include the meta description,
Open Graph tags, JSON-LD `Person` data and `hreflang` links. Set `SITE["url"]` in
`content.py` to your deployed URL to also emit canonical / `og:image` tags.

## Project structure

```
portfolio_wajd_updated/
├── app.py              # Streamlit entry point (language via ?lang=en|ar)
├── build.py            # Static site generator → dist/
├── components.py       # HTML components (shared by app.py and build.py)
├── content.py          # All content, English + Arabic — edit this to update the site
├── static/
│   ├── style.css       # Design system: tokens, light/dark, RTL, responsive
│   └── profile.jpg     # Profile photo (served by Streamlit at /app/static/)
└── .streamlit/config.toml
```

## Updating content

Everything lives in `content.py`. Empty optional fields are hidden, so you can fill
them in as you go:

- Project `links`: `{"code": "https://github.com/...", "demo": "https://..."}` adds buttons.
- Project `contribution` / `impact`: shown as extra rows on the project card.
- Certification `url`: makes the certificate name a verification link.
- Look for `# TODO` comments for details that still need your input.

## Notes

- The theme toggle is CSS-only (works inside Streamlit, which strips scripts); the
  static build also remembers the choice in `localStorage`.
- Streamlit renders pages client-side, so search engines see little of it — deploy the
  static build if SEO matters.
