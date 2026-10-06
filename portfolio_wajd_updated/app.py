"""Streamlit entry point: `streamlit run app.py`.

The page itself is plain HTML/CSS produced by components.py; Streamlit only
serves it. The language is chosen with the `?lang=en|ar` query parameter so the
language switch is a normal link that works without a rerun callback.
"""

from pathlib import Path

import streamlit as st

import components
from content import CONTENT, DEFAULT_LANGUAGE, LANGUAGES

ROOT = Path(__file__).parent

# Hide Streamlit's own chrome so the page reads as a normal website.
STREAMLIT_OVERRIDES = """
#MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"],
[data-testid="stStatusWidget"] { display: none !important; }
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] { background: var(--bg) !important; }
[data-testid="stMainBlockContainer"], .block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
[data-testid="stElementContainer"] { width: 100% !important; }
@media (prefers-reduced-motion: no-preference) {
  [data-testid="stMain"], [data-testid="stAppViewContainer"] { scroll-behavior: smooth; }
}
"""


@st.cache_data
def load_css():
    return (ROOT / "static" / "style.css").read_text(encoding="utf-8")


lang = st.query_params.get("lang", DEFAULT_LANGUAGE)
if lang not in LANGUAGES:
    lang = DEFAULT_LANGUAGE
data = CONTENT[lang]
other = next(code for code in LANGUAGES if code != lang)

st.set_page_config(
    page_title=data["meta"]["title"],
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    f"<style>@import url('{components.FONTS_URL}');\n{load_css()}\n{STREAMLIT_OVERRIDES}</style>"
    + components.page(
        data,
        lang,
        asset_base="app/static/",
        alt_lang_href=f"?lang={other}",
        alt_lang_code=other,
    )
)
