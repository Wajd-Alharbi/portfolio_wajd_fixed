"""All portfolio content, in English and Arabic.

Edit this file to update the site. Every text value is plain text (it is
HTML-escaped when rendered). Optional fields that are empty ("" / [] / {})
are simply not shown, so leave a field empty rather than inventing content.
"""

# ---------------------------------------------------------------------------
# Language-independent data
# ---------------------------------------------------------------------------

SITE = {
    # Public URL of the deployed static site, e.g. "https://wajd-alharbi.github.io/portfolio".
    # Used for canonical / Open Graph tags in build.py. Leave empty if unknown.
    "url": "",
    "email": "wajd.mazen.alharbi@gmail.com",
    "linkedin": "https://www.linkedin.com/in/wajd-alharbi-/",
    "github": "https://github.com/Wajd-Alharbi",
    "photo": "profile.jpg",  # file inside static/
}


CONTENT = {
    # =======================================================================
    # ENGLISH
    # =======================================================================
    "en": {
        "lang_name": "English",
        "switch_label": "العربية",
        "meta": {
            "title": "Wajd Mazen Alharbi — AI Engineer · Automation & Agentic AI",
            "description": (
                "Wajd Mazen Alharbi is an AI Engineer focused on agentic AI, LLM "
                "applications and automation — building intelligent systems that "
                "automate real-world workflows."
            ),
        },
        "ui": {
            "skip": "Skip to content",
            "menu": "Sections",
            "theme": "Toggle light / dark theme",
            "problem": "Problem",
            "solution": "Solution",
            "contribution": "My contribution",
            "impact": "Impact",
            "code": "Code",
            "demo": "Live demo",
            "more_projects": "More projects",
            "all_github": "More on GitHub",
            "back_to_top": "Back to top",
            "issued": "Issued",
            "featured": "Featured",
            "verify": "Verify credential",
        },
        "nav": [
            ("about", "About"),
            ("experience", "Experience"),
            ("projects", "Projects"),
            ("skills", "Skills"),
            ("education", "Education"),
            ("certifications", "Certifications"),
            ("volunteering", "Volunteering"),
            ("contact", "Contact"),
        ],
        "hero": {
            "name": "Wajd Mazen Alharbi",
            "role": "AI Engineer · Automation & Agentic AI",
            "headline": "I build intelligent systems that automate real-world work.",
            "intro": (
                "I design agentic workflows, LLM-powered applications and machine "
                "learning models that take repetitive, data-heavy processes off "
                "people's plates — and hold up outside the notebook."
            ),
            "status": "Open to AI engineering roles",
            "location": "Jeddah, Saudi Arabia",
            "primary_cta": "View my work",
            "secondary_cta": "Contact me",
            "facts": [
                ("B.Sc. AI", "University of Jeddah"),
                ("4.92 / 5", "Cumulative GPA"),
                ("NVIDIA-Certified", "Generative AI & LLMs"),
                ("Digital Transformation", "Jeddah Municipality"),
            ],
        },
        "about": {
            "kicker": "About",
            "title": "Engineering AI that does useful work.",
            "paragraphs": [
                (
                    "I'm an Artificial Intelligence graduate from the University of "
                    "Jeddah, where I studied Computer Science & Engineering with a "
                    "specialization in AI."
                ),
                (
                    "What drives me is the step after the model: turning machine "
                    "learning, LLMs and autonomous agents into systems that plug into "
                    "real workflows. I've applied this in multi-agent and RAG projects, "
                    "in Arabic NLP and computer vision, and during Digital "
                    "Transformation training at Jeddah Municipality."
                ),
                (
                    "I approach every project the same way — understand the workflow, "
                    "find where intelligence or automation removes friction, then build "
                    "and measure something people can actually use."
                ),
            ],
            "principles": [
                ("Workflow first", "Start from the real process and the people in it, not from the model."),
                ("Systems, not demos", "Agents, retrieval and models wired together into something dependable."),
                ("Measured results", "Evaluate against the problem — accuracy, time saved, effort removed."),
            ],
            "languages_label": "Languages",
            "languages": "Arabic (native) · English (professional)",
        },
        "experience": {
            "kicker": "Experience",
            "title": "Practical experience in a professional environment.",
            "items": [
                {
                    "role": "Digital Transformation Trainee",
                    "org": "Jeddah Municipality",
                    "date": "Jun 2025 – Aug 2025",
                    "summary": (
                        "Applied AI and automation within the municipality's digital "
                        "transformation efforts, working on practical solutions for "
                        "internal processes."
                    ),
                    "points": [
                        "Developed an intelligent HR chatbot.",
                        "Built smart solutions to improve the efficiency of internal workflows.",
                        "Enhanced a CNN model for waste detection, reaching 95% accuracy.",
                    ],
                    "tags": ["Digital Transformation", "Automation", "Chatbots", "Computer Vision"],
                },
            ],
        },
        "projects": {
            "kicker": "Selected work",
            "title": "Projects",
            "intro": "Agentic systems, retrieval and applied machine learning — built around a concrete problem.",
            "featured": [
                {
                    "title": "Autonomous Multi-Agent Framework for Smart Campus",
                    "category": "Agentic AI",
                    "summary": "A framework where autonomous AI agents work alongside machine learning models to detect anomalies across smart-campus operations.",
                    "problem": "Campus operations produce continuous streams of data, and unusual behaviour is hard to spot and act on through manual monitoring alone.",
                    "solution": "Autonomous agents coordinate with LSTM and XGBoost models to detect anomalies, combining learned detection with agent-driven reasoning and follow-up.",
                    "contribution": "",  # TODO: describe your role (e.g. architecture, agents, models)
                    "impact": "",  # TODO: add a result if you have one
                    "tags": ["AI Agents", "Multi-Agent Systems", "LSTM", "XGBoost", "Anomaly Detection"],
                    "links": {},  # e.g. {"code": "https://github.com/...", "demo": "https://..."}
                },
                {
                    "title": "AI-Powered Automation for GDG on Campus",
                    "category": "Automation",
                    "summary": "AI-driven automation for the administration of the Google Developer Groups (GDG) on Campus club.",
                    "problem": "Running a student tech community involves recurring administrative work that takes organizers' time away from the community itself.",
                    "solution": "AI-powered automation that takes over routine administrative tasks, so organizers can focus on events and members.",
                    "contribution": "",  # TODO
                    "impact": "",  # TODO
                    "tags": ["Automation", "Generative AI", "Workflow Design"],
                    "links": {},
                },
                {
                    "title": "RAG File Q&A",
                    "category": "Generative AI",
                    "summary": "A retrieval-augmented generation app for asking natural-language questions about your own files.",
                    "problem": "Finding a specific answer inside long documents is slow, and a general-purpose LLM can't see private files and may hallucinate.",
                    "solution": "Documents are indexed for semantic search; relevant passages are retrieved and passed to an LLM so answers are grounded in the uploaded content.",
                    "contribution": "",  # TODO
                    "impact": "",  # TODO
                    "tags": ["RAG", "LLMs", "FAISS", "Python"],  # TODO: confirm the exact stack
                    "links": {},
                },
                {
                    "title": "SeCor — POI Recommendation System",
                    "category": "Recommender Systems",
                    "summary": "Semantic-Enhanced Collaborative Filtering: a hybrid recommender for points of interest.",
                    "problem": "Pure collaborative filtering struggles with sparse interaction data and ignores what places actually are.",
                    "solution": "A hybrid model that combines semantic information about points of interest with collaborative filtering to produce more relevant recommendations.",
                    "contribution": "",  # TODO
                    "impact": "",  # TODO
                    "tags": ["Recommender Systems", "Collaborative Filtering", "Machine Learning"],
                    "links": {},
                },
            ],
            "more": [
                {
                    "title": "Smart Complaint Classifier",
                    "summary": "Classifies Arabic complaints automatically using AraBERT and Transformer techniques.",
                    "tags": ["Arabic NLP", "AraBERT", "Transformers"],
                    "links": {},
                },
                {
                    "title": "Vision-Based Waste Detection",
                    "summary": "CNN-based detection and classification of urban waste — enhanced to 95% accuracy during training at Jeddah Municipality.",
                    "tags": ["Computer Vision", "CNN", "Deep Learning"],
                    "links": {},
                },
            ],
        },
        "skills": {
            "kicker": "Skills",
            "title": "Toolkit",
            "categories": [
                ("Generative AI & LLMs", ["Large Language Models", "RAG", "Prompt Engineering", "Transformers", "AraBERT"]),
                ("Automation & Agentic AI", ["Autonomous Agents", "Multi-Agent Systems", "Workflow Automation", "Chatbots"]),
                ("Machine Learning & Deep Learning", ["Deep Learning", "CNNs", "LSTM", "XGBoost", "Anomaly Detection", "Recommender Systems"]),
                ("Data, NLP & Vision", ["NLP", "Arabic NLP", "Computer Vision", "Data Analysis", "Vector Search (FAISS)"]),
                ("Programming & Tools", ["Python", "SQL", "FAISS", "Power BI"]),
                ("Professional", ["Analytical Thinking", "Problem Solving", "Leadership", "Strategic Planning", "Teamwork"]),
            ],
        },
        "education": {
            "kicker": "Education",
            "title": "Academic foundation",
            "degree": "Bachelor of Computer Science & Engineering — Artificial Intelligence",
            "school": "University of Jeddah",
            "date": "Aug 2021 – May 2026",
            "gpa_label": "GPA",
            "gpa": "4.92 / 5",
            "focus": "Machine Learning · Deep Learning · NLP · Computer Vision · Data Science",
        },
        "certifications": {
            "kicker": "Certifications",
            "title": "Professional certifications",
            "items": [
                {
                    "name": "NVIDIA-Certified Associate: Generative AI & LLMs",
                    "issuer": "NVIDIA",
                    "date": "Jul 2026",
                    "text": "Professional certification from NVIDIA in Generative AI and Large Language Models.",
                    "url": "",  # TODO: add the credential verification link
                },
            ],
        },
        "volunteering": {
            "kicker": "Volunteering",
            "title": "Volunteering & community partnerships",
            "intro": "Supporting the student tech community through technical initiatives, education and AI solutions.",
            "items": [
                {
                    "type": "Community partnership",
                    "org": "GDG on Campus — University of Jeddah",
                    "text": "Contributing to technical initiatives and developing AI-based solutions, including automation for club administration.",
                    "highlight": None,
                    "tags": ["Technical Initiatives", "AI Solutions", "Automation"],
                },
                {
                    "type": "Volunteering & leadership",
                    "org": "AI Club",
                    "text": "Leading educational and technical initiatives in artificial intelligence.",
                    "highlight": ("950+", "participants reached"),
                    "tags": ["Leadership", "Education", "Technical Initiatives"],
                },
            ],
        },
        "contact": {
            "kicker": "Contact",
            "title": "Let's build something intelligent.",
            "text": "I'm looking for opportunities in AI engineering, automation and agentic AI. The fastest way to reach me is email — I'm also happy to connect on LinkedIn.",
            "email_label": "Email",
            "linkedin_label": "LinkedIn",
            "linkedin_handle": "in/wajd-alharbi-",
            "github_label": "GitHub",
            "github_handle": "Wajd-Alharbi",
        },
        "footer": "Wajd Mazen Alharbi · AI Engineer",
    },
    # =======================================================================
    # ARABIC
    # =======================================================================
    "ar": {
        "lang_name": "العربية",
        "switch_label": "English",
        "meta": {
            "title": "وجد مازن الحربي — مهندسة ذكاء اصطناعي · الأتمتة والوكلاء الأذكياء",
            "description": (
                "وجد مازن الحربي مهندسة ذكاء اصطناعي تركّز على الوكلاء الأذكياء وتطبيقات "
                "النماذج اللغوية الكبيرة والأتمتة، وتبني أنظمة ذكية تؤتمت مسارات العمل الواقعية."
            ),
        },
        "ui": {
            "skip": "تخطَّ إلى المحتوى",
            "menu": "الأقسام",
            "theme": "تبديل الوضع الفاتح / الداكن",
            "problem": "المشكلة",
            "solution": "الحل",
            "contribution": "مساهمتي",
            "impact": "الأثر",
            "code": "الكود",
            "demo": "عرض مباشر",
            "more_projects": "مشاريع أخرى",
            "all_github": "المزيد على GitHub",
            "back_to_top": "العودة للأعلى",
            "issued": "تاريخ الإصدار",
            "featured": "مميز",
            "verify": "التحقق من الشهادة",
        },
        "nav": [
            ("about", "نبذة"),
            ("experience", "الخبرة"),
            ("projects", "المشاريع"),
            ("skills", "المهارات"),
            ("education", "التعليم"),
            ("certifications", "الشهادات"),
            ("volunteering", "التطوع"),
            ("contact", "التواصل"),
        ],
        "hero": {
            "name": "وجد مازن الحربي",
            "role": "مهندسة ذكاء اصطناعي · الأتمتة والوكلاء الأذكياء",
            "headline": "أبني أنظمة ذكية تؤتمت العمل في الواقع.",
            "intro": (
                "أصمّم مسارات عمل قائمة على الوكلاء الأذكياء، وتطبيقات مدعومة بالنماذج "
                "اللغوية الكبيرة، ونماذج تعلّم آلة تتولّى العمليات المتكررة والمعتمدة على "
                "البيانات — وتعمل بكفاءة خارج بيئة التجربة."
            ),
            "status": "متاحة لفرص هندسة الذكاء الاصطناعي",
            "location": "جدة، المملكة العربية السعودية",
            "primary_cta": "استعرض أعمالي",
            "secondary_cta": "تواصل معي",
            "facts": [
                ("بكالوريوس ذكاء اصطناعي", "جامعة جدة"),
                ("\u20664.92 / 5\u2069", "المعدل التراكمي"),
                ("شهادة NVIDIA", "الذكاء التوليدي والنماذج اللغوية"),
                ("التحول الرقمي", "أمانة محافظة جدة"),
            ],
        },
        "about": {
            "kicker": "نبذة",
            "title": "ذكاء اصطناعي يُنجز عملاً مفيدًا.",
            "paragraphs": [
                (
                    "خريجة ذكاء اصطناعي من جامعة جدة، درستُ علوم وهندسة الحاسب بتخصص "
                    "الذكاء الاصطناعي."
                ),
                (
                    "ما يحفّزني هو الخطوة التي تلي بناء النموذج: تحويل تعلّم الآلة والنماذج "
                    "اللغوية الكبيرة والوكلاء الأذكياء إلى أنظمة تندمج في مسارات العمل الفعلية. "
                    "طبّقتُ ذلك في مشاريع الأنظمة متعددة الوكلاء وRAG، ومعالجة اللغة العربية "
                    "والرؤية الحاسوبية، وخلال تدريبي في التحول الرقمي بأمانة محافظة جدة."
                ),
                (
                    "أتعامل مع كل مشروع بالطريقة نفسها: أفهم مسار العمل، وأحدد أين يزيل الذكاء "
                    "الاصطناعي أو الأتمتة العوائق، ثم أبني حلًا قابلًا للاستخدام وأقيس أثره."
                ),
            ],
            "principles": [
                ("مسار العمل أولًا", "أبدأ من العملية الحقيقية والأشخاص فيها، لا من النموذج."),
                ("أنظمة لا عروض", "وكلاء واسترجاع ونماذج تعمل معًا في نظام يُعتمد عليه."),
                ("نتائج قابلة للقياس", "التقييم وفق المشكلة: الدقة، والوقت الموفَّر، والجهد المُزال."),
            ],
            "languages_label": "اللغات",
            "languages": "العربية (اللغة الأم) · الإنجليزية (كفاءة مهنية)",
        },
        "experience": {
            "kicker": "الخبرة",
            "title": "خبرة عملية في بيئة مهنية.",
            "items": [
                {
                    "role": "متدربة في التحول الرقمي",
                    "org": "أمانة محافظة جدة",
                    "date": "يونيو 2025 – أغسطس 2025",
                    "summary": (
                        "طبّقتُ الذكاء الاصطناعي والأتمتة ضمن جهود التحول الرقمي في الأمانة، "
                        "وعملتُ على حلول عملية للعمليات الداخلية."
                    ),
                    "points": [
                        "تطوير روبوت محادثة ذكي للموارد البشرية.",
                        "بناء حلول ذكية لرفع كفاءة سير العمل الداخلي.",
                        "تحسين نموذج CNN للكشف عن النفايات لتصل دقته إلى 95%.",
                    ],
                    "tags": ["التحول الرقمي", "الأتمتة", "روبوتات المحادثة", "الرؤية الحاسوبية"],
                },
            ],
        },
        "projects": {
            "kicker": "أعمال مختارة",
            "title": "المشاريع",
            "intro": "أنظمة وكلاء أذكياء، واسترجاع معلومات، وتعلّم آلة تطبيقي — كلٌّ منها مبني حول مشكلة محددة.",
            "featured": [
                {
                    "title": "Autonomous Multi-Agent Framework for Smart Campus",
                    "category": "الوكلاء الأذكياء",
                    "summary": "إطار عمل يعمل فيه وكلاء ذكاء اصطناعي مستقلون جنبًا إلى جنب مع نماذج تعلّم الآلة لاكتشاف الحالات الشاذة في عمليات الحرم الجامعي الذكي.",
                    "problem": "تُنتج عمليات الحرم الجامعي تدفقات مستمرة من البيانات، ويصعب رصد السلوك غير الطبيعي والتعامل معه بالمراقبة اليدوية وحدها.",
                    "solution": "وكلاء مستقلون يتنسّقون مع نموذجَي LSTM وXGBoost لاكتشاف الحالات الشاذة، بالجمع بين الكشف المتعلَّم والاستدلال والمتابعة عبر الوكلاء.",
                    "contribution": "",
                    "impact": "",
                    "tags": ["AI Agents", "Multi-Agent Systems", "LSTM", "XGBoost", "Anomaly Detection"],
                    "links": {},
                },
                {
                    "title": "AI-Powered Automation for GDG on Campus",
                    "category": "الأتمتة",
                    "summary": "أتمتة مدعومة بالذكاء الاصطناعي للأعمال الإدارية لنادي مجتمعات مطوّري Google ‏(GDG on Campus).",
                    "problem": "إدارة مجتمع تقني طلابي تتضمن أعمالًا إدارية متكررة تستهلك وقت المنظمين على حساب المجتمع نفسه.",
                    "solution": "أتمتة مدعومة بالذكاء الاصطناعي تتولى المهام الإدارية الروتينية، ليتفرغ المنظمون للفعاليات والأعضاء.",
                    "contribution": "",
                    "impact": "",
                    "tags": ["Automation", "Generative AI", "Workflow Design"],
                    "links": {},
                },
                {
                    "title": "RAG File Q&A",
                    "category": "الذكاء التوليدي",
                    "summary": "تطبيق قائم على التوليد المعزّز بالاسترجاع (RAG) لطرح أسئلة بلغة طبيعية حول ملفاتك.",
                    "problem": "البحث عن إجابة محددة داخل مستندات طويلة بطيء، ونموذج اللغة العام لا يرى الملفات الخاصة وقد يختلق الإجابات.",
                    "solution": "تُفهرس المستندات للبحث الدلالي، ثم تُسترجع المقاطع ذات الصلة وتُمرَّر إلى النموذج اللغوي لتستند الإجابات إلى محتوى الملفات.",
                    "contribution": "",
                    "impact": "",
                    "tags": ["RAG", "LLMs", "FAISS", "Python"],
                    "links": {},
                },
                {
                    "title": "SeCor — POI Recommendation System",
                    "category": "أنظمة التوصية",
                    "summary": "الترشيح التعاوني المعزّز دلاليًا: نظام توصية هجين للأماكن ونقاط الاهتمام.",
                    "problem": "يواجه الترشيح التعاوني وحده صعوبة مع البيانات المتفرقة ويتجاهل طبيعة الأماكن نفسها.",
                    "solution": "نموذج هجين يدمج المعلومات الدلالية عن نقاط الاهتمام مع الترشيح التعاوني لتقديم توصيات أكثر ملاءمة.",
                    "contribution": "",
                    "impact": "",
                    "tags": ["Recommender Systems", "Collaborative Filtering", "Machine Learning"],
                    "links": {},
                },
            ],
            "more": [
                {
                    "title": "Smart Complaint Classifier",
                    "summary": "تصنيف تلقائي للشكاوى العربية باستخدام AraBERT وتقنيات Transformer.",
                    "tags": ["Arabic NLP", "AraBERT", "Transformers"],
                    "links": {},
                },
                {
                    "title": "Vision-Based Waste Detection",
                    "summary": "كشف النفايات الحضرية وتصنيفها باستخدام CNN — حُسّن ليصل إلى دقة 95% خلال التدريب في أمانة محافظة جدة.",
                    "tags": ["Computer Vision", "CNN", "Deep Learning"],
                    "links": {},
                },
            ],
        },
        "skills": {
            "kicker": "المهارات",
            "title": "الأدوات والمهارات",
            "categories": [
                ("الذكاء التوليدي والنماذج اللغوية", ["Large Language Models", "RAG", "Prompt Engineering", "Transformers", "AraBERT"]),
                ("الأتمتة والوكلاء الأذكياء", ["Autonomous Agents", "Multi-Agent Systems", "Workflow Automation", "Chatbots"]),
                ("تعلّم الآلة والتعلّم العميق", ["Deep Learning", "CNNs", "LSTM", "XGBoost", "Anomaly Detection", "Recommender Systems"]),
                ("البيانات واللغة والرؤية", ["NLP", "Arabic NLP", "Computer Vision", "Data Analysis", "Vector Search (FAISS)"]),
                ("البرمجة والأدوات", ["Python", "SQL", "FAISS", "Power BI"]),
                ("مهارات مهنية", ["التفكير التحليلي", "حل المشكلات", "القيادة", "التخطيط الاستراتيجي", "العمل الجماعي"]),
            ],
        },
        "education": {
            "kicker": "التعليم",
            "title": "الأساس الأكاديمي",
            "degree": "بكالوريوس علوم وهندسة الحاسب — الذكاء الاصطناعي",
            "school": "جامعة جدة",
            "date": "أغسطس 2021 – مايو 2026",
            "gpa_label": "المعدل",
            "gpa": "\u20664.92 / 5\u2069",
            "focus": "تعلّم الآلة · التعلّم العميق · معالجة اللغة الطبيعية · الرؤية الحاسوبية · علم البيانات",
        },
        "certifications": {
            "kicker": "الشهادات",
            "title": "الشهادات الاحترافية",
            "items": [
                {
                    "name": "NVIDIA-Certified Associate: Generative AI & LLMs",
                    "issuer": "NVIDIA",
                    "date": "يوليو 2026",
                    "text": "شهادة احترافية من NVIDIA في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة.",
                    "url": "",
                },
            ],
        },
        "volunteering": {
            "kicker": "التطوع",
            "title": "التطوع والشراكات المجتمعية",
            "intro": "دعم المجتمع التقني الطلابي عبر المبادرات التقنية والتعليم وحلول الذكاء الاصطناعي.",
            "items": [
                {
                    "type": "شراكة مجتمعية",
                    "org": "GDG on Campus — جامعة جدة",
                    "text": "المساهمة في المبادرات التقنية وتطوير حلول قائمة على الذكاء الاصطناعي، منها أتمتة الأعمال الإدارية للنادي.",
                    "highlight": None,
                    "tags": ["مبادرات تقنية", "حلول ذكاء اصطناعي", "الأتمتة"],
                },
                {
                    "type": "تطوع وقيادة",
                    "org": "نادي الذكاء الاصطناعي",
                    "text": "قيادة مبادرات تعليمية وتقنية في مجال الذكاء الاصطناعي.",
                    "highlight": ("950+", "مشاركًا استفادوا من المبادرات"),
                    "tags": ["القيادة", "التعليم", "مبادرات تقنية"],
                },
            ],
        },
        "contact": {
            "kicker": "التواصل",
            "title": "لنبنِ شيئًا ذكيًا معًا.",
            "text": "أبحث عن فرص في هندسة الذكاء الاصطناعي والأتمتة والوكلاء الأذكياء. أسرع طريقة للتواصل معي هي البريد الإلكتروني، ويسعدني التواصل عبر LinkedIn أيضًا.",
            "email_label": "البريد الإلكتروني",
            "linkedin_label": "LinkedIn",
            "linkedin_handle": "in/wajd-alharbi-",
            "github_label": "GitHub",
            "github_handle": "Wajd-Alharbi",
        },
        "footer": "وجد مازن الحربي · مهندسة ذكاء اصطناعي",
    },
}

LANGUAGES = tuple(CONTENT)
DEFAULT_LANGUAGE = "en"
