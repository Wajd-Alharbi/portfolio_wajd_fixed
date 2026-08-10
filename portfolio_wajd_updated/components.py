import streamlit as st

def hero_section(data, lang_dir="ltr"):
    # Use profile.png if it exists, otherwise placeholder
    img_path = "assets/profile.png"
    
    st.markdown(
        f"""
        <div class="hero" dir="{lang_dir}">
            <div class="hero-content">
                <div class="hero-text-side">
                    <div class="hero-eyebrow">{data['eyebrow']}</div>
                    <h1 class="hero-title">
                        {data['title_part1']}
                        <span class="hero-gradient">{data['title_gradient']}</span>
                        {data['title_part2']}
                    </h1>
                    <p class="hero-description">{data['description']}</p>
                    <div class="hero-buttons">
                        <a href="https://www.linkedin.com/in/wajd-alharbi-/" target="_blank" class="hero-button primary-button">{data['primary_btn']}</a>
                        <a href="mailto:wajd.mazen.alharbi@gmail.com" class="hero-button secondary-button">{data['secondary_btn']}</a>
                    </div>
                </div>
                <div class="hero-image-side">
                    <div class="hero-image-container">
                        <img src="portfolio_wajd_updated/app/assets/profile.png" class="hero-profile-img" onerror="this.src='https://via.placeholder.com/400?text=Wajd+Alharbi'">
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_header(title, subtitle, lang_dir="ltr"):
    st.markdown(f'<div class="section-title" dir="{lang_dir}">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-subtitle" dir="{lang_dir}">{subtitle}</div>', unsafe_allow_html=True)

def info_card(icon, title, text, lang_dir="ltr"):
    icon_html = f"""
<div class="card-icon">
    {icon}
</div>
""" if icon else ""

    html = f"""
<div class="info-card" dir="{lang_dir}">
    {icon_html}

    <div class="card-title">
        {title}
    </div>

    <div class="card-text">
        {text}
    </div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )

def project_card(number, title, description, tags, lang_dir="ltr"):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(
        f"""
        <div class="project-card" dir="{lang_dir}">
            <div class="project-number">{number}</div>
            <div class="project-title">{title}</div>
            <div class="project-description">
                {description}
                <br><br>
                <div class="project-tags">{tags_html}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def timeline_item(title, date, text, lang_dir="ltr"):
    date_html = f'<div class="timeline-date">{date}</div>' if date else ""
    st.markdown(
        f"""
        <div class="timeline-item" dir="{lang_dir}">
            <div class="timeline-title">{title}</div>
            {date_html}
            <div class="timeline-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def skill_category(name, skills, lang_dir="ltr"):
    skills_html = "".join([f'<span class="tag skill-tag">{skill}</span>' for skill in skills])
    st.markdown(
        f"""
        <div class="skill-category-card" dir="{lang_dir}">
            <div class="category-name">{name}</div>
            <div class="skills-grid">
                {skills_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def language_toggle(current_lang):
    # This will now be styled to appear in the corner
    is_arabic = current_lang == "Arabic"
    
    btn_label = "EN / AR"
    
    # We use a unique key and wrap it in a div for positioning via CSS
    st.markdown('<div class="floating-lang-toggle">', unsafe_allow_html=True)
    if st.button(btn_label, key="lang_toggle_btn"):
        st.markdown('</div>', unsafe_allow_html=True)
        return True
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def sidebar_profile(data):
    st.markdown(
        f"""
        <div class="profile-card">
            <div class="profile-avatar-container">
                <img src="file/app/assets/profile.png" class="profile-avatar" onerror="this.src='https://via.placeholder.com/150?text=WA'">
            </div>
            <div class="profile-name">{data['name']}</div>
            <div class="profile-role">{data['role']}</div>
            <div class="availability">
                <span class="availability-dot"></span>
                {data['availability']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def social_links():
    st.markdown(
        """
        <div class="social-links-container">
            <a class="social-btn linkedin" href="https://www.linkedin.com/in/wajd-alharbi-/" target="_blank">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
            <a class="social-btn github" href="https://github.com/Wajd-Alharbi" target="_blank">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a class="social-btn x-twitter" href="https://x.com/" target="_blank">
                <i class="fab fa-x-twitter"></i> X
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
