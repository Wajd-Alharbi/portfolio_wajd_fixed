"""Build a static, SEO-friendly version of the portfolio.

    python build.py            # writes ./dist

Produces dist/index.html (English), dist/ar/index.html (Arabic) and copies
static/ next to them. The output is plain HTML/CSS (plus a tiny script that
remembers the theme choice), ready for GitHub Pages, Netlify, Vercel, etc.
It uses the same components and stylesheet as the Streamlit app.
"""

import json
import shutil
from html import escape
from pathlib import Path

import components
from content import CONTENT, DEFAULT_LANGUAGE, LANGUAGES, SITE

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

THEME_SCRIPT = """<script>
(function () {
  var box = document.getElementById("theme-toggle");
  try { box.checked = localStorage.getItem("theme-flipped") === "1"; } catch (e) {}
  box.addEventListener("change", function () {
    try { localStorage.setItem("theme-flipped", box.checked ? "1" : "0"); } catch (e) {}
  });
})();
</script>"""


def page_path(lang):
    return "" if lang == DEFAULT_LANGUAGE else f"{lang}/"


def head(lang, data, css):
    meta = data["meta"]
    url = SITE["url"].rstrip("/")
    tags = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{escape(meta['title'])}</title>",
        f'<meta name="description" content="{escape(meta["description"])}">',
        f'<meta name="author" content="{escape(CONTENT["en"]["hero"]["name"])}">',
        '<meta name="color-scheme" content="light dark">',
        '<meta name="theme-color" content="#fafaf9" media="(prefers-color-scheme: light)">',
        '<meta name="theme-color" content="#0b0c0e" media="(prefers-color-scheme: dark)">',
        '<meta property="og:type" content="profile">',
        f'<meta property="og:title" content="{escape(meta["title"])}">',
        f'<meta property="og:description" content="{escape(meta["description"])}">',
        f'<meta property="og:locale" content="{"ar_SA" if lang == "ar" else "en_US"}">',
        '<meta name="twitter:card" content="summary">',
        "<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' rx='8' fill='%23111113'/%3E%3Ctext x='16' y='22' font-family='monospace' "
        "font-size='17' font-weight='700' text-anchor='middle' fill='%23fff'%3EW%3C/text%3E%3C/svg%3E\">",
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        f'<link rel="stylesheet" href="{components.FONTS_URL}">',
    ]
    if url:
        tags += [
            f'<link rel="canonical" href="{url}/{page_path(lang)}">',
            f'<meta property="og:url" content="{url}/{page_path(lang)}">',
            f'<meta property="og:image" content="{url}/static/{SITE["photo"]}">',
        ]
        tags += [
            f'<link rel="alternate" hreflang="{code}" href="{url}/{page_path(code)}">' for code in LANGUAGES
        ]
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": CONTENT["en"]["hero"]["name"],
        "jobTitle": "AI Engineer",
        "email": f"mailto:{SITE['email']}",
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "University of Jeddah"},
        "knowsAbout": ["Artificial Intelligence", "Agentic AI", "Automation", "Large Language Models",
                       "Machine Learning", "Deep Learning", "Natural Language Processing"],
        "sameAs": [SITE["linkedin"], SITE["github"]],
    }
    if url:
        person["url"] = url
    tags.append(f'<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>')
    tags.append(f"<style>{css}</style>")
    return "\n".join(tags)


def build():
    css = (ROOT / "static" / "style.css").read_text(encoding="utf-8")
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST / "static")

    for lang in LANGUAGES:
        data = CONTENT[lang]
        other = next(code for code in LANGUAGES if code != lang)
        depth = "../" if page_path(lang) else ""
        body = components.page(
            data,
            lang,
            asset_base=f"{depth}static/",
            alt_lang_href=f"{depth}{page_path(other)}" or "./",
            alt_lang_code=other,
        )
        direction = "rtl" if lang == "ar" else "ltr"
        html = (
            f'<!doctype html>\n<html lang="{lang}" dir="{direction}">\n<head>\n{head(lang, data, css)}\n</head>\n'
            f"<body>\n{body}\n{THEME_SCRIPT}\n</body>\n</html>\n"
        )
        out = DIST / page_path(lang) / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
