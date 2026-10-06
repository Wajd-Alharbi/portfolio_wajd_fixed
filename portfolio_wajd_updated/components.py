"""Reusable UI components.

Each function returns an HTML string; nothing here depends on Streamlit, so the
same markup is used by the Streamlit app (app.py) and the static build (build.py).
All text coming from content.py is escaped here.
"""

from html import escape

from content import SITE

FONTS_URL = (
    "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500"
    "&family=IBM+Plex+Sans+Arabic:wght@400;500;600&display=swap"
)


def _e(text):
    return escape(str(text), quote=True)


def _external(href, label, cls="", extra=""):
    return (
        f'<a class="{cls}" href="{_e(href)}" target="_blank" rel="noopener noreferrer"{extra}>'
        f"{label}</a>"
    )


def icon(name):
    return f'<span class="icon icon-{name}" aria-hidden="true"></span>'


def tags(items, cls="tags"):
    if not items:
        return ""
    chips = "".join(f"<li>{_e(t)}</li>" for t in items)
    return f'<ul class="{cls}">{chips}</ul>'


def section_head(index, kicker, title, intro="", heading_id=""):
    intro_html = f'<p class="section-intro">{_e(intro)}</p>' if intro else ""
    return (
        '<header class="section-head">'
        f'<p class="kicker"><span class="kicker-index">{index:02d}</span>{_e(kicker)}</p>'
        f'<h2 id="{heading_id}">{_e(title)}</h2>'
        f"{intro_html}"
        "</header>"
    )


def link_buttons(links, ui):
    """Code / demo buttons; renders nothing when a project has no links."""
    labels = {"code": (ui["code"], "github"), "demo": (ui["demo"], "external")}
    out = []
    for key, (label, ico) in labels.items():
        if links.get(key):
            out.append(
                _external(
                    links[key],
                    f"{icon(ico)}<span>{_e(label)}</span>",
                    cls="btn btn-small btn-ghost",
                )
            )
    return f'<div class="project-links">{"".join(out)}</div>' if out else ""


# ---------------------------------------------------------------------------
# Page chrome
# ---------------------------------------------------------------------------

def topbar(data, alt_lang_href, alt_lang_code):
    ui = data["ui"]
    links = "".join(f'<li><a href="#{key}">{_e(label)}</a></li>' for key, label in data["nav"])
    return (
        '<header class="topbar">'
        '<div class="container topbar-inner">'
        f'<a class="brand" href="#top" aria-label="{_e(data["hero"]["name"])}">'
        '<span class="brand-mark" aria-hidden="true">W</span>'
        f'<span class="brand-name">{_e(data["hero"]["name"])}</span>'
        "</a>"
        f'<nav class="nav" aria-label="{_e(ui["menu"])}"><ul>{links}</ul></nav>'
        '<div class="topbar-actions">'
        f'<a class="lang-switch" href="{_e(alt_lang_href)}" hreflang="{alt_lang_code}" '
        f'lang="{alt_lang_code}">{_e(data["switch_label"])}</a>'
        f'<label class="theme-btn" for="theme-toggle" title="{_e(ui["theme"])}">'
        f'{icon("moon")}{icon("sun")}<span class="sr-only">{_e(ui["theme"])}</span></label>'
        "</div>"
        "</div>"
        "</header>"
    )


def footer(data):
    ui = data["ui"]
    return (
        '<footer class="footer">'
        '<div class="container footer-inner">'
        f"<p>© 2026 {_e(data['footer'])}</p>"
        f'<a href="#top">{_e(ui["back_to_top"])} ↑</a>'
        "</div>"
        "</footer>"
    )


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------

def agent_trace():
    """Decorative illustration of an agentic workflow run (hidden from screen readers)."""
    steps = [
        ("trigger", "new request received"),
        ("plan", "split task into steps"),
        ("retrieve", "fetch context from docs"),
        ("act", "call tools · update records"),
        ("report", "summarize & hand off"),
    ]
    rows = "".join(
        f'<li style="--i:{i}"><span class="trace-status"></span>'
        f'<span class="trace-step">{step}</span><span class="trace-msg">{msg}</span></li>'
        for i, (step, msg) in enumerate(steps)
    )
    return (
        '<div class="trace" aria-hidden="true" dir="ltr">'
        '<div class="trace-head">'
        '<span class="trace-dots"><i></i><i></i><i></i></span>'
        '<span class="trace-title">agent.run — workflow</span>'
        "</div>"
        f'<ol class="trace-steps">{rows}</ol>'
        '<div class="trace-foot"><span>LLM</span><span>tools</span><span>memory</span>'
        "<span>human review</span></div>"
        "</div>"
    )


def hero(data):
    h = data["hero"]
    facts = "".join(
        f'<li><span class="fact-value">{_e(v)}</span><span class="fact-label">{_e(l)}</span></li>'
        for v, l in h["facts"]
    )
    return (
        '<section class="hero" id="top" aria-labelledby="hero-title">'
        '<div class="container">'
        '<div class="hero-grid">'
        '<div class="hero-copy">'
        f'<p class="status"><span class="status-dot" aria-hidden="true"></span>{_e(h["status"])}'
        f'<span class="status-sep" aria-hidden="true">·</span>{_e(h["location"])}</p>'
        f'<h1 id="hero-title" class="hero-name">{_e(h["name"])}</h1>'
        f'<p class="hero-role">{_e(h["role"])}</p>'
        f'<p class="hero-headline">{_e(h["headline"])}</p>'
        f'<p class="hero-intro">{_e(h["intro"])}</p>'
        '<div class="hero-ctas">'
        f'<a class="btn btn-primary" href="#projects">{_e(h["primary_cta"])}{icon("arrow")}</a>'
        f'<a class="btn btn-ghost" href="#contact">{_e(h["secondary_cta"])}</a>'
        "</div>"
        "</div>"
        f'<div class="hero-visual">{agent_trace()}</div>'
        "</div>"
        f'<ul class="facts">{facts}</ul>'
        "</div>"
        "</section>"
    )


def about(data, asset_base):
    a = data["about"]
    paragraphs = "".join(f"<p>{_e(p)}</p>" for p in a["paragraphs"])
    principles = "".join(
        f"<li><h3>{_e(t)}</h3><p>{_e(d)}</p></li>" for t, d in a["principles"]
    )
    return (
        '<section class="section" id="about" aria-labelledby="about-title">'
        '<div class="container about-grid">'
        '<figure class="portrait">'
        f'<img src="{_e(asset_base)}{_e(SITE["photo"])}" alt="{_e(data["hero"]["name"])}" '
        'width="720" height="827" loading="lazy" decoding="async">'
        f'<figcaption><span>{_e(a["languages_label"])}</span>{_e(a["languages"])}</figcaption>'
        "</figure>"
        '<div class="about-copy">'
        + section_head(1, a["kicker"], a["title"], heading_id="about-title")
        + f'<div class="prose">{paragraphs}</div>'
        f'<ul class="principles">{principles}</ul>'
        "</div>"
        "</div>"
        "</section>"
    )


def experience(data):
    x = data["experience"]
    items = ""
    for item in x["items"]:
        points = "".join(f"<li>{_e(p)}</li>" for p in item["points"])
        items += (
            '<article class="role">'
            '<div class="role-meta">'
            f'<p class="role-date">{_e(item["date"])}</p>'
            f'<p class="role-org">{_e(item["org"])}</p>'
            "</div>"
            '<div class="role-body">'
            f"<h3>{_e(item['role'])}</h3>"
            f'<p class="role-summary">{_e(item["summary"])}</p>'
            f'<ul class="role-points">{points}</ul>'
            f"{tags(item['tags'])}"
            "</div>"
            "</article>"
        )
    leadership = "".join(
        f'<li><h4>{_e(l["org"])}</h4><p>{_e(l["text"])}</p></li>' for l in x["leadership"]
    )
    return (
        '<section class="section section-alt" id="experience" aria-labelledby="experience-title">'
        '<div class="container">'
        + section_head(2, x["kicker"], x["title"], heading_id="experience-title")
        + f'<div class="roles">{items}</div>'
        f'<h3 class="subhead">{_e(x["leadership_title"])}</h3>'
        f'<ul class="leadership">{leadership}</ul>'
        "</div>"
        "</section>"
    )


def project_card(index, project, ui):
    details = ""
    for key in ("problem", "solution", "contribution", "impact"):
        if project.get(key):
            details += f'<div class="detail detail-{key}"><dt>{_e(ui[key])}</dt><dd>{_e(project[key])}</dd></div>'
    return (
        '<article class="project">'
        '<div class="project-main">'
        '<div class="project-top">'
        f'<span class="project-index" aria-hidden="true">{index:02d}</span>'
        f'<p class="project-cat">{_e(project["category"])}</p>'
        "</div>"
        f"<h3>{_e(project['title'])}</h3>"
        f'<p class="project-summary">{_e(project["summary"])}</p>'
        f"{tags(project['tags'])}"
        f"{link_buttons(project.get('links', {}), ui)}"
        "</div>"
        f'<dl class="project-details">{details}</dl>'
        "</article>"
    )


def mini_project(project, ui):
    return (
        '<article class="mini-project">'
        f"<h4>{_e(project['title'])}</h4>"
        f"<p>{_e(project['summary'])}</p>"
        f"{tags(project['tags'], 'tags tags-quiet')}"
        f"{link_buttons(project.get('links', {}), ui)}"
        "</article>"
    )


def projects(data):
    p, ui = data["projects"], data["ui"]
    featured = "".join(project_card(i, proj, ui) for i, proj in enumerate(p["featured"], 1))
    more = "".join(mini_project(proj, ui) for proj in p["more"])
    github = _external(
        SITE["github"],
        f"{icon('github')}<span>{_e(ui['all_github'])}</span>{icon('external')}",
        cls="text-link",
    )
    return (
        '<section class="section" id="projects" aria-labelledby="projects-title">'
        '<div class="container">'
        + section_head(3, p["kicker"], p["title"], p["intro"], heading_id="projects-title")
        + f'<div class="project-list">{featured}</div>'
        '<div class="more-head">'
        f'<h3 class="subhead">{_e(ui["more_projects"])}</h3>{github}'
        "</div>"
        f'<div class="more-grid">{more}</div>'
        "</div>"
        "</section>"
    )


def skills(data):
    s = data["skills"]
    cards = "".join(
        f'<li class="skill-group"><h3>{_e(name)}</h3>{tags(items, "tags tags-quiet")}</li>'
        for name, items in s["categories"]
    )
    return (
        '<section class="section section-alt" id="skills" aria-labelledby="skills-title">'
        '<div class="container">'
        + section_head(4, s["kicker"], s["title"], heading_id="skills-title")
        + f'<ul class="skill-grid">{cards}</ul>'
        "</div>"
        "</section>"
    )


def education(data):
    ed, ui = data["education"], data["ui"]
    certs = ""
    for c in ed["certs"]:
        name = _e(c["name"])
        if c.get("url"):
            name = _external(c["url"], f"{name}{icon('external')}", cls="text-link")
        certs += (
            '<li class="cert">'
            f'<span class="cert-badge" aria-hidden="true">{_e(c["issuer"][:1])}</span>'
            f'<div><h4>{name}</h4><p>{_e(c["issuer"])} · {_e(ui["issued"])} {_e(c["date"])}</p></div>'
            "</li>"
        )
    return (
        '<section class="section" id="education" aria-labelledby="education-title">'
        '<div class="container">'
        + section_head(5, ed["kicker"], ed["title"], heading_id="education-title")
        + '<div class="edu-grid">'
        '<article class="card degree">'
        f'<p class="degree-school">{_e(ed["school"])}</p>'
        f"<h3>{_e(ed['degree'])}</h3>"
        f'<p class="degree-date">{_e(ed["date"])}</p>'
        f'<p class="degree-gpa"><span>{_e(ed["gpa_label"])}</span><strong>{_e(ed["gpa"])}</strong></p>'
        f'<p class="degree-focus">{_e(ed["focus"])}</p>'
        "</article>"
        '<article class="card certs" id="certifications">'
        f'<h3 class="card-title">{_e(ed["certs_title"])}</h3>'
        f'<ul class="cert-list">{certs}</ul>'
        "</article>"
        "</div>"
        "</div>"
        "</section>"
    )


def contact(data):
    c = data["contact"]
    rows = [
        (f"mailto:{SITE['email']}", "mail", c["email_label"], SITE["email"], False),
        (SITE["linkedin"], "linkedin", c["linkedin_label"], c["linkedin_handle"], True),
        (SITE["github"], "github", c["github_label"], c["github_handle"], True),
    ]
    items = ""
    for href, ico, label, value, external in rows:
        inner = (
            f'{icon(ico)}<span class="contact-label">{_e(label)}</span>'
            f'<span class="contact-value" dir="ltr">{_e(value)}</span>{icon("arrow")}'
        )
        link = (
            _external(href, inner, cls="contact-link")
            if external
            else f'<a class="contact-link" href="{_e(href)}">{inner}</a>'
        )
        items += f"<li>{link}</li>"
    return (
        '<section class="section section-alt contact" id="contact" aria-labelledby="contact-title">'
        '<div class="container contact-grid">'
        "<div>"
        + section_head(6, c["kicker"], c["title"], heading_id="contact-title")
        + f'<p class="contact-text">{_e(c["text"])}</p>'
        "</div>"
        f'<ul class="contact-list">{items}</ul>'
        "</div>"
        "</section>"
    )


# ---------------------------------------------------------------------------
# Full page body
# ---------------------------------------------------------------------------

def page(data, lang, *, asset_base, alt_lang_href, alt_lang_code):
    """The complete page body.

    asset_base:    URL prefix where files from static/ are served.
    alt_lang_href: link to the same page in the other language.
    """
    direction = "rtl" if lang == "ar" else "ltr"
    return (
        f'<div class="site" lang="{lang}" dir="{direction}">'
        # Checkbox drives the CSS-only theme toggle (see `:has(#theme-toggle:checked)` in style.css)
        f'<input type="checkbox" id="theme-toggle" class="theme-input sr-only" aria-label="{_e(data["ui"]["theme"])}">'
        f'<a class="skip-link" href="#main">{_e(data["ui"]["skip"])}</a>'
        + topbar(data, alt_lang_href, alt_lang_code)
        + '<main id="main">'
        + hero(data)
        + about(data, asset_base)
        + experience(data)
        + projects(data)
        + skills(data)
        + education(data)
        + contact(data)
        + "</main>"
        + footer(data)
        + "</div>"
    )
