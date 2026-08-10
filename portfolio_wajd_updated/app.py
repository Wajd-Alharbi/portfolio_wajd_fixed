import streamlit as st
import os

from content import CONTENT
import components


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Wajd Alharbi | AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SESSION STATE
# =========================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "page" not in st.session_state:
    st.session_state.page = "Home"


# =========================================================
# LOAD CSS & ASSETS
# =========================================================

def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# Add Font Awesome for icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
    unsafe_allow_html=True
)

css_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "style.css"
)

local_css(css_path)


# =========================================================
# DATA & DIRECTION
# =========================================================

lang = st.session_state.language
data = CONTENT[lang]
lang_dir = "rtl" if lang == "Arabic" else "ltr"


# =========================================================
# FLOATING LANGUAGE TOGGLE (Top Corner)
# =========================================================

if components.language_toggle(lang):
    if lang == "English":
        st.session_state.language = "Arabic"
    else:
        st.session_state.language = "English"
    
    # Reset page to Home after language change
    st.session_state.page = "Home"
    st.rerun()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # Profile
    components.sidebar_profile(
        data["profile"]
    )

    st.markdown("---")

    # =====================================================
    # NAVIGATION
    # =====================================================

    for label, page in data["menu"].items():

        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True
        ):
            st.session_state.page = page
            st.rerun()

    st.markdown("---")
    
    # =====================================================
    # SOCIAL LINKS
    # =====================================================
    components.social_links()


# =========================================================
# MAIN CONTENT
# =========================================================

page = st.session_state.page


# =========================================================
# HOME
# =========================================================

if page == "Home":

    components.hero_section(
        data["home"]["hero"],
        lang_dir
    )

    components.section_header(
        "At a Glance"
        if lang == "English"
        else "نظرة سريعة",

        "A quick overview of my journey."
        if lang == "English"
        else "نظرة سريعة على مسيرتي.",

        lang_dir
    )

    cols = st.columns(4)

    for i, stat in enumerate(
        data["home"]["stats"]
    ):

        with cols[i % 4]:

            components.info_card(
                stat.get("icon"),
                stat["title"],
                stat["text"],
                lang_dir
            )

    components.section_header(
        "Areas of Expertise"
        if lang == "English"
        else "مجالات الخبرة",

        "Key domains I focus on."
        if lang == "English"
        else "المجالات الرئيسية التي أركز عليها.",

        lang_dir
    )

    cols = st.columns(3)

    for i, area in enumerate(
        data["home"]["focus_areas"]
    ):

        with cols[i % 3]:

            components.info_card(
                area.get("icon"),
                area["title"],
                area["text"],
                lang_dir
            )


# =========================================================
# EDUCATION
# =========================================================

elif page == "Education":

    components.section_header(
        data["education"]["title"],
        data["education"]["subtitle"],
        lang_dir
    )

    st.markdown(
        '<div class="timeline-container">',
        unsafe_allow_html=True
    )

    for item in data["education"]["items"]:

        components.timeline_item(
            item["title"],
            item["date"],
            item["text"],
            lang_dir
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# EXPERIENCE
# =========================================================

elif page == "Experience":

    components.section_header(
        data["experience"]["title"],
        data["experience"]["subtitle"],
        lang_dir
    )

    st.markdown(
        '<div class="timeline-container">',
        unsafe_allow_html=True
    )

    for item in data["experience"]["items"]:

        components.timeline_item(
            item["title"],
            item["date"],
            item["text"],
            lang_dir
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# PROJECTS
# =========================================================

elif page == "Projects":

    components.section_header(
        data["projects"]["title"],
        data["projects"]["subtitle"],
        lang_dir
    )

    items = data["projects"]["items"]

    for i in range(0, len(items), 2):

        cols = st.columns(2)

        for j in range(2):

            if i + j < len(items):

                project = items[i + j]

                with cols[j]:

                    components.project_card(
                        project["number"],
                        project["title"],
                        project["description"],
                        project["tags"],
                        lang_dir
                    )


# =========================================================
# CERTIFICATIONS
# =========================================================

elif page == "Certifications":

    components.section_header(
        data["certifications"]["title"],
        data["certifications"]["subtitle"],
        lang_dir
    )

    items = data["certifications"]["items"]

    cols = st.columns(
        min(len(items), 3)
    )

    for i, item in enumerate(items):

        with cols[i % len(cols)]:

            components.info_card(
                item.get("icon"),
                item["title"],
                item["text"],
                lang_dir
            )


# =========================================================
# VOLUNTEERING
# =========================================================

elif page == "Volunteering":

    components.section_header(
        data["volunteering"]["title"],
        data["volunteering"]["subtitle"],
        lang_dir
    )

    st.markdown(
        '<div class="timeline-container">',
        unsafe_allow_html=True
    )

    for item in data["volunteering"]["items"]:

        components.timeline_item(
            item["title"],
            None,
            item["text"],
            lang_dir
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# SKILLS
# =========================================================

elif page == "Skills":

    components.section_header(
        data["skills"]["title"],
        data["skills"]["subtitle"],
        lang_dir
    )

    categories = data["skills"]["categories"]

    for i in range(0, len(categories), 2):

        cols = st.columns(2)

        for j in range(2):

            if i + j < len(categories):

                category = categories[i + j]

                with cols[j]:

                    components.skill_category(
                        category["name"],
                        category["skills"],
                        lang_dir
                    )


# =========================================================
# LANGUAGES
# =========================================================

elif page == "Languages":

    components.section_header(
        data["languages"]["title"],
        data["languages"]["subtitle"],
        lang_dir
    )

    items = data["languages"]["items"]

    cols = st.columns(
        len(items)
    )

    for i, item in enumerate(items):

        with cols[i]:

            components.info_card(
                None,
                item["title"],
                item["text"],
                lang_dir
            )


# =========================================================
# CONTACT
# =========================================================

elif page == "Contact":

    cdata = data["contact"]

    st.markdown(
        f"""
        <div class="contact-header" dir="{lang_dir}">

            <h2>
                {cdata['title']}
            </h2>

            <p>
                {cdata['description']}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    with st.form(
        f"contact_form_{lang}"
    ):

        name = st.text_input(
            cdata["form"]["name"]
        )

        email = st.text_input(
            cdata["form"]["email"]
        )

        message = st.text_area(
            cdata["form"]["message"],
            height=150
        )

        submitted = st.form_submit_button(
            cdata["form"]["submit"],
            use_container_width=True
        )

        if submitted:

            if name and email and message:

                st.success(
                    cdata["form"]["success"]
                )

            else:

                st.warning(
                    cdata["form"]["error"]
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    f"""
    <footer class="site-footer" dir="{lang_dir}">
        {data['footer']}
    </footer>
    """,
    unsafe_allow_html=True
)
