"""All portfolio content, in English and Arabic.

Edit this file to update the site. Every text value is plain text (it is
HTML-escaped when rendered). Optional fields that are empty ("" / [] / {} / None)
are simply not shown, so leave a field empty rather than inventing content.

Facts, figures and links come from the CV (WAJD_ALHARBI_Resume.docx).
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
    "github_repos": "https://github.com/Wajd-Alharbi?tab=repositories",
    "photo": "profile.jpg",  # file inside static/
}

# Verification links from the CV
LINKS = {
    "degree": "https://drive.google.com/file/d/1QwFYTNm3o-V5e1qTvepw03oUSBtVnH84/view?usp=drive_link",
    "english": "https://drive.google.com/file/d/1FPZPpnvZKMG6ESD1jiV4ochWL1Kya7-j/view?usp=drive_link",
    "nca_genl": "https://www.credly.com/badges/58a6accf-d351-4710-8ece-06764ddfbfb7/public_url",
    "course_eda": "https://www.coursera.org/account/accomplishments/verify/NS118ZFFMXBJ",
    "course_dnn": "https://www.coursera.org/account/accomplishments/verify/Z7W2TQ1S8RBM",
    "course_plotting": "https://www.coursera.org/account/accomplishments/verify/S6SR218J73LT",
    "course_llm_prompt": "https://learn.nvidia.com/certificates?id=J7Q42PbTTw2VGJKYbRgrqQ",
    "course_transformer_nlp": "https://learn.nvidia.com/certificates?id=PVY-Oz2DSEiE0LOJZlauPA",
}

# Arabic text: wrap numbers like "4.92 / 5" in LRI…PDI so they keep reading left-to-right.
LTR = "⁦{}⁩".format


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
            "code": "Code",
            "demo": "Live demo",
            "more_projects": "More projects",
            "all_github": "All repositories on GitHub",
            "back_to_top": "Back to top",
            "issued": "Issued",
            "verify": "Verify credential",
            "view_certificate": "View degree certificate",
            "courses": "Courses",
            "verify_short": "Verify",
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
                "I design autonomous agents, LLM-powered applications and machine "
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
                ("AI Engineer Intern", "Jeddah Municipality"),
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
                    "real workflows. I've applied this in agentic AI, RAG and "
                    "recommender projects, in Arabic NLP and computer vision, and as an "
                    "AI Engineer intern in the Digital Transformation Department at "
                    "Jeddah Municipality."
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
            "languages_link": ("English proficiency — verification", LINKS["english"]),
        },
        "experience": {
            "kicker": "Experience",
            "title": "Practical experience in a professional environment.",
            "items": [
                {
                    "role": "AI Engineer Intern",
                    "org": "Jeddah Municipality",
                    "dept": "Digital Transformation Department",
                    "date": "Jun 2025 – Jul 2025",
                    "summary": (
                        "Built AI and automation solutions for the municipality's Digital "
                        "Transformation Department — from an HR chatbot to a computer "
                        "vision model and a new internal communication platform."
                    ),
                    "metrics": [
                        ("60%", "of HR inquiries automated"),
                        ("50%", "fewer lost requests"),
                        ("95%", "waste-detection accuracy"),
                    ],
                    "points": [
                        "Engineered an intelligent HR chatbot using semantic search and NLP, automating 60% of inquiries and reducing response time by 40%.",
                        "Designed and deployed a centralized communication platform replacing phone-based requests, improving workflow transparency by 70% and reducing lost requests by 50%.",
                        "Improved and optimized a CNN-based waste-detection model to 95% accuracy, reducing reliance on manual monitoring by 60% and increasing response speed by 30%.",
                    ],
                    "tags": ["Chatbots", "Semantic Search", "NLP", "Computer Vision", "Digital Transformation"],
                },
            ],
        },
        "projects": {
            "kicker": "Selected work",
            "title": "Projects",
            "intro": "Agentic systems, retrieval and applied machine learning — each built around a concrete problem and measured against it.",
            "featured": [
                {
                    "title": "Agentic AI with Autonomous Agents",
                    "category": "Agentic AI",
                    "summary": "An autonomous agent for operational monitoring that forecasts expected behaviour and detects genuine anomalies.",
                    "problem": "Anomaly detection in operational monitoring systems is unreliable — false alerts increase workload and reduce trust.",
                    "solution": "An autonomous agent combining XGBoost forecasting with LSTM anomaly detection on a fully optimized data-processing pipeline.",
                    "contribution": "",
                    "metrics": [("92%", "detection accuracy"), ("−35%", "false alerts"), ("60 days", "of data, minimal memory")],
                    "tags": ["Autonomous Agents", "XGBoost", "LSTM", "Anomaly Detection", "Data Pipelines"],
                    "links": {},  # e.g. {"code": "https://github.com/...", "demo": "https://..."}
                },
                {
                    "title": "Applicant Evaluation Agent — GDG on Campus",
                    "category": "Automation",
                    "summary": "An autonomous agent tool deployed for the GDG on Campus Automation Committee that evaluates and ranks event applicants.",
                    "problem": "Filtering event applicants by hand was slow and hard to apply consistently.",
                    "solution": "The agent scores each applicant with eligibility metrics, preference scoring and rule-based decision logic, then ranks them for the organizers.",
                    "contribution": "Deployed the tool for the Automation Committee of Google Developer Groups on Campus.",
                    "metrics": [("70%", "more efficient applicant filtering")],
                    "tags": ["Autonomous Agents", "Rule-Based Logic", "Scoring & Ranking", "Automation"],
                    "links": {},
                },
                {
                    "title": "Intelligent Educational RAG System",
                    "category": "Generative AI · RAG",
                    "summary": "A retrieval-augmented Q&A system for asking questions about large educational documents and PDFs.",
                    "problem": "Retrieving relevant information from large educational documents is slow, which holds back learning and access to content.",
                    "solution": "LLMs with FAISS vector search and custom embedding pipelines, optimized for large-scale PDF processing, ground every answer in the source material.",
                    "contribution": "",
                    "metrics": [("0.89", "MRR"), ("0.87", "Precision@3")],
                    "tags": ["RAG", "LLMs", "FAISS", "Embeddings", "PDF Processing"],
                    "links": {},
                },
                {
                    "title": "Smart Complaint Classifier",
                    "category": "Arabic NLP",
                    "summary": "Classifies Arabic complaints and routes them to the right department, with explainable predictions.",
                    "problem": "Complaint triage across multi-department service environments was slow and inconsistent.",
                    "solution": "An Arabic NLP pipeline built with AraBERT, TF-IDF and Logistic Regression, using SHAP and LIME to explain each decision.",
                    "contribution": "",
                    "metrics": [("−87%", "misclassification"), ("+40%", "issue-diagnosis efficiency")],
                    "tags": ["Arabic NLP", "AraBERT", "TF-IDF", "Logistic Regression", "SHAP", "LIME"],
                    "links": {},
                },
                {
                    "title": "SeCor — Semantic-Enhanced Collaborative Filtering",
                    "category": "Recommender Systems",
                    "summary": "A hybrid point-of-interest recommender that adds LLM-based semantic embeddings to collaborative filtering.",
                    "problem": "Cold start: new users or items have too little history, so recommendations become inaccurate.",
                    "solution": "Hybrid recommendation modeling that combines collaborative filtering with LLM-based semantic embeddings.",
                    "contribution": "",
                    "metrics": [("−32%", "cold-start error"), ("−18%", "RMSE"), ("+21%", "NDCG@K")],
                    "tags": ["Recommender Systems", "Collaborative Filtering", "LLM Embeddings", "Hybrid Modeling"],
                    "links": {},
                },
            ],
            "more": [
                {
                    "title": "Vision-Based Waste Detection",
                    "summary": "CNN-based detection and classification of urban waste — optimized to 95% accuracy during the Jeddah Municipality internship.",
                    "tags": ["Computer Vision", "CNN", "Deep Learning"],
                    "links": {},
                },
            ],
        },
        "skills": {
            "kicker": "Skills",
            "title": "Toolkit",
            "categories": [
                ("Generative AI & LLMs", ["Large Language Models", "Generative AI", "RAG", "Prompt Engineering", "Embeddings", "Transformers"]),
                ("Agentic AI & Automation", ["Autonomous Agents", "Rule-Based Decision Logic", "Chatbots", "Workflow Automation"]),
                ("Machine Learning & Deep Learning", ["Machine Learning", "ANN", "CNN", "LSTM", "XGBoost", "Logistic Regression", "Anomaly Detection", "Recommender Systems", "SHAP / LIME"]),
                ("Natural Language Processing", ["NLP", "Arabic NLP", "AraBERT", "TF-IDF", "Semantic Search"]),
                ("Computer Vision", ["Computer Vision", "CNN", "Object Detection", "Image Classification"]),
                ("Data & Analytics", ["Power BI", "Data Cleaning", "Data Visualization", "Exploratory Data Analysis", "Dashboards"]),
                ("Programming & Tools", ["Python", "Java / JavaScript", "C / C++", "SQL", "FAISS"]),
                ("Soft Skills", ["Analytical Thinking", "Strategic Planning", "Leadership & Ownership", "Stakeholder Communication", "Problem Structuring", "Time & Priority Management"]),
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
            "certificate_url": LINKS["degree"],
        },
        "certifications": {
            "kicker": "Certifications",
            "title": "Professional certifications",
            "items": [
                {
                    "name": "NVIDIA-Certified Associate: Generative AI LLMs",
                    "code": "NCA-GENL",
                    "issuer": "NVIDIA",
                    "date": "Jul 2026",
                    "text": "Professional certification from NVIDIA in Generative AI and Large Language Models.",
                    "url": LINKS["nca_genl"],
                },
            ],
            "courses": [
                ("Building LLM Applications with Prompt Engineering", "NVIDIA", "May 2026", LINKS["course_llm_prompt"]),
                ("Introduction to Transformer-Based Natural Language Processing", "NVIDIA", "May 2026", LINKS["course_transformer_nlp"]),
                ("Exploratory Data Analysis for Machine Learning", "Coursera", "Nov 2024", LINKS["course_eda"]),
                ("Improving Deep Neural Networks", "Coursera", "Nov 2024", LINKS["course_dnn"]),
                ("Plotting, Charting & Data Representation", "Coursera", "Nov 2024", LINKS["course_plotting"]),
            ],
        },
        "volunteering": {
            "kicker": "Volunteering",
            "title": "Volunteering & community partnerships",
            "intro": "Supporting the student tech community through education, technical initiatives and AI tools.",
            "items": [
                {
                    "org": "Artificial Intelligence Club",
                    "role": "Planning & Communication",
                    "date": "Sep 2024 – Jun 2026",
                    "text": "Led AI educational initiatives, including content development for a large-scale university bootcamp and hands-on machine learning workshops for high-school students.",
                    "highlight": ("950+", "participants impacted"),
                    "tags": ["Leadership", "Content Development", "ML Workshops"],
                },
                {
                    "org": "Google Developer Groups on Campus",
                    "role": "Automation Committee",
                    "date": "Mar 2026 – Jul 2026",
                    "text": "Deployed an autonomous agent tool that evaluates and ranks event applicants using eligibility metrics, preference scoring and rule-based decision logic.",
                    "highlight": ("70%", "more efficient applicant filtering"),
                    "tags": ["Autonomous Agents", "Automation", "Community"],
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
            "code": "الكود",
            "demo": "عرض مباشر",
            "more_projects": "مشاريع أخرى",
            "all_github": "جميع المستودعات على GitHub",
            "back_to_top": "العودة للأعلى",
            "issued": "تاريخ الإصدار",
            "verify": "التحقق من الشهادة",
            "view_certificate": "عرض وثيقة التخرج",
            "courses": "الدورات",
            "verify_short": "تحقق",
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
                "أصمّم وكلاء أذكياء مستقلين، وتطبيقات مدعومة بالنماذج اللغوية الكبيرة، "
                "ونماذج تعلّم آلة تتولّى العمليات المتكررة والمعتمدة على البيانات — "
                "وتعمل بكفاءة خارج بيئة التجربة."
            ),
            "status": "متاحة لفرص هندسة الذكاء الاصطناعي",
            "location": "جدة، المملكة العربية السعودية",
            "primary_cta": "استعرض أعمالي",
            "secondary_cta": "تواصل معي",
            "facts": [
                ("بكالوريوس ذكاء اصطناعي", "جامعة جدة"),
                (LTR("4.92 / 5"), "المعدل التراكمي"),
                ("شهادة NVIDIA", "الذكاء التوليدي والنماذج اللغوية"),
                ("مهندسة ذكاء اصطناعي متدربة", "أمانة محافظة جدة"),
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
                    "طبّقتُ ذلك في مشاريع الوكلاء الأذكياء وRAG وأنظمة التوصية، وفي معالجة "
                    "اللغة العربية والرؤية الحاسوبية، وخلال تدريبي مهندسةَ ذكاء اصطناعي في "
                    "إدارة التحول الرقمي بأمانة محافظة جدة."
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
            "languages_link": ("إثبات الكفاءة في اللغة الإنجليزية", LINKS["english"]),
        },
        "experience": {
            "kicker": "الخبرة",
            "title": "خبرة عملية في بيئة مهنية.",
            "items": [
                {
                    "role": "مهندسة ذكاء اصطناعي (متدربة)",
                    "org": "أمانة محافظة جدة",
                    "dept": "إدارة التحول الرقمي",
                    "date": "يونيو 2025 – يوليو 2025",
                    "summary": (
                        "بنيتُ حلول ذكاء اصطناعي وأتمتة لإدارة التحول الرقمي في الأمانة — "
                        "من روبوت محادثة للموارد البشرية إلى نموذج رؤية حاسوبية ومنصة "
                        "تواصل داخلية جديدة."
                    ),
                    "metrics": [
                        ("60%", "من استفسارات الموارد البشرية مؤتمتة"),
                        ("50%", "انخفاض في الطلبات المفقودة"),
                        ("95%", "دقة كشف النفايات"),
                    ],
                    "points": [
                        "تطوير روبوت محادثة ذكي للموارد البشرية باستخدام البحث الدلالي ومعالجة اللغة الطبيعية، أتمت 60% من الاستفسارات وخفّض زمن الاستجابة بنسبة 40%.",
                        "تصميم وإطلاق منصة تواصل مركزية بديلة عن الطلبات الهاتفية، رفعت شفافية سير العمل بنسبة 70% وخفّضت الطلبات المفقودة بنسبة 50%.",
                        "تحسين نموذج CNN للكشف عن النفايات لتصل دقته إلى 95%، مع تقليل الاعتماد على المراقبة اليدوية بنسبة 60% وزيادة سرعة الاستجابة بنسبة 30%.",
                    ],
                    "tags": ["روبوتات المحادثة", "البحث الدلالي", "NLP", "الرؤية الحاسوبية", "التحول الرقمي"],
                },
            ],
        },
        "projects": {
            "kicker": "أعمال مختارة",
            "title": "المشاريع",
            "intro": "أنظمة وكلاء أذكياء، واسترجاع معلومات، وتعلّم آلة تطبيقي — كلٌّ منها مبني حول مشكلة محددة ومُقاس بنتائجها.",
            "featured": [
                {
                    "title": "Agentic AI with Autonomous Agents",
                    "category": "الوكلاء الأذكياء",
                    "summary": "وكيل ذكي مستقل لمراقبة العمليات، يتنبأ بالسلوك المتوقع ويكتشف الحالات الشاذة الحقيقية.",
                    "problem": "اكتشاف الحالات الشاذة في أنظمة مراقبة العمليات غير موثوق، والتنبيهات الكاذبة تزيد عبء العمل وتُضعف الثقة بالنظام.",
                    "solution": "وكيل مستقل يجمع بين التنبؤ بـ XGBoost واكتشاف الشذوذ بـ LSTM، ضمن مسار معالجة بيانات محسَّن بالكامل.",
                    "contribution": "",
                    "metrics": [("92%", "دقة الاكتشاف"), ("−35%", "التنبيهات الكاذبة"), ("60 يومًا", "من البيانات بأقل استهلاك للذاكرة")],
                    "tags": ["Autonomous Agents", "XGBoost", "LSTM", "Anomaly Detection", "Data Pipelines"],
                    "links": {},
                },
                {
                    "title": "Applicant Evaluation Agent — GDG on Campus",
                    "category": "الأتمتة",
                    "summary": "أداة وكيل ذكي مستقل أُطلقت للجنة الأتمتة في GDG on Campus لتقييم المتقدمين للفعاليات وترتيبهم.",
                    "problem": "فرز المتقدمين للفعاليات يدويًا كان بطيئًا ويصعب تطبيقه بشكل متسق.",
                    "solution": "يقيّم الوكيل كل متقدم وفق معايير الأهلية وتقييم التفضيلات ومنطق قرار قائم على القواعد، ثم يرتّبهم للمنظمين.",
                    "contribution": "إطلاق الأداة للجنة الأتمتة في Google Developer Groups on Campus.",
                    "metrics": [("70%", "رفع كفاءة فرز المتقدمين")],
                    "tags": ["Autonomous Agents", "Rule-Based Logic", "Scoring & Ranking", "Automation"],
                    "links": {},
                },
                {
                    "title": "Intelligent Educational RAG System",
                    "category": "الذكاء التوليدي · RAG",
                    "summary": "نظام أسئلة وأجوبة قائم على التوليد المعزّز بالاسترجاع للبحث في المستندات التعليمية الكبيرة وملفات PDF.",
                    "problem": "استرجاع المعلومات ذات الصلة من المستندات التعليمية الكبيرة بطيء، مما يعيق التعلّم والوصول إلى المحتوى.",
                    "solution": "نماذج لغوية كبيرة مع بحث متجهي عبر FAISS ومسارات تضمين مخصصة، محسّنة لمعالجة ملفات PDF على نطاق واسع، لتستند كل إجابة إلى المصدر.",
                    "contribution": "",
                    "metrics": [("0.89", "MRR"), ("0.87", "Precision@3")],
                    "tags": ["RAG", "LLMs", "FAISS", "Embeddings", "PDF Processing"],
                    "links": {},
                },
                {
                    "title": "Smart Complaint Classifier",
                    "category": "معالجة اللغة العربية",
                    "summary": "يصنّف الشكاوى العربية ويوجّهها إلى الإدارة المختصة، مع تفسير لكل قرار.",
                    "problem": "فرز الشكاوى في بيئات الخدمة متعددة الإدارات كان بطيئًا وغير متسق.",
                    "solution": "مسار لمعالجة اللغة العربية مبني بـ AraBERT وTF-IDF والانحدار اللوجستي، مع SHAP وLIME لتفسير كل قرار.",
                    "contribution": "",
                    "metrics": [("−87%", "أخطاء التصنيف"), ("+40%", "كفاءة تشخيص المشكلات")],
                    "tags": ["Arabic NLP", "AraBERT", "TF-IDF", "Logistic Regression", "SHAP", "LIME"],
                    "links": {},
                },
                {
                    "title": "SeCor — Semantic-Enhanced Collaborative Filtering",
                    "category": "أنظمة التوصية",
                    "summary": "نظام توصية هجين لنقاط الاهتمام يضيف تضمينات دلالية مبنية على النماذج اللغوية إلى الترشيح التعاوني.",
                    "problem": "مشكلة البداية الباردة: المستخدمون أو العناصر الجديدة بلا سجل كافٍ، فتصبح التوصيات غير دقيقة.",
                    "solution": "نمذجة توصية هجينة تجمع بين الترشيح التعاوني والتضمينات الدلالية المبنية على النماذج اللغوية الكبيرة.",
                    "contribution": "",
                    "metrics": [("−32%", "خطأ البداية الباردة"), ("−18%", "RMSE"), ("+21%", "NDCG@K")],
                    "tags": ["Recommender Systems", "Collaborative Filtering", "LLM Embeddings", "Hybrid Modeling"],
                    "links": {},
                },
            ],
            "more": [
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
                ("الذكاء التوليدي والنماذج اللغوية", ["Large Language Models", "Generative AI", "RAG", "Prompt Engineering", "Embeddings", "Transformers"]),
                ("الوكلاء الأذكياء والأتمتة", ["Autonomous Agents", "Rule-Based Decision Logic", "Chatbots", "Workflow Automation"]),
                ("تعلّم الآلة والتعلّم العميق", ["Machine Learning", "ANN", "CNN", "LSTM", "XGBoost", "Logistic Regression", "Anomaly Detection", "Recommender Systems", "SHAP / LIME"]),
                ("معالجة اللغة الطبيعية", ["NLP", "Arabic NLP", "AraBERT", "TF-IDF", "Semantic Search"]),
                ("الرؤية الحاسوبية", ["Computer Vision", "CNN", "Object Detection", "Image Classification"]),
                ("البيانات والتحليلات", ["Power BI", "Data Cleaning", "Data Visualization", "Exploratory Data Analysis", "Dashboards"]),
                ("البرمجة والأدوات", ["Python", "Java / JavaScript", "C / C++", "SQL", "FAISS"]),
                ("المهارات الشخصية", ["التفكير التحليلي", "التخطيط الاستراتيجي", "القيادة وتحمّل المسؤولية", "التواصل مع أصحاب المصلحة", "هيكلة المشكلات", "إدارة الوقت والأولويات"]),
            ],
        },
        "education": {
            "kicker": "التعليم",
            "title": "الأساس الأكاديمي",
            "degree": "بكالوريوس علوم وهندسة الحاسب — الذكاء الاصطناعي",
            "school": "جامعة جدة",
            "date": "أغسطس 2021 – مايو 2026",
            "gpa_label": "المعدل",
            "gpa": LTR("4.92 / 5"),
            "focus": "تعلّم الآلة · التعلّم العميق · معالجة اللغة الطبيعية · الرؤية الحاسوبية · علم البيانات",
            "certificate_url": LINKS["degree"],
        },
        "certifications": {
            "kicker": "الشهادات",
            "title": "الشهادات الاحترافية",
            "items": [
                {
                    "name": "NVIDIA-Certified Associate: Generative AI LLMs",
                    "code": "NCA-GENL",
                    "issuer": "NVIDIA",
                    "date": "يوليو 2026",
                    "text": "شهادة احترافية من NVIDIA في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة.",
                    "url": LINKS["nca_genl"],
                },
            ],
            "courses": [
                ("Building LLM Applications with Prompt Engineering", "NVIDIA", "مايو 2026", LINKS["course_llm_prompt"]),
                ("Introduction to Transformer-Based Natural Language Processing", "NVIDIA", "مايو 2026", LINKS["course_transformer_nlp"]),
                ("Exploratory Data Analysis for Machine Learning", "Coursera", "نوفمبر 2024", LINKS["course_eda"]),
                ("Improving Deep Neural Networks", "Coursera", "نوفمبر 2024", LINKS["course_dnn"]),
                ("Plotting, Charting & Data Representation", "Coursera", "نوفمبر 2024", LINKS["course_plotting"]),
            ],
        },
        "volunteering": {
            "kicker": "التطوع",
            "title": "التطوع والشراكات المجتمعية",
            "intro": "دعم المجتمع التقني الطلابي عبر التعليم والمبادرات التقنية وأدوات الذكاء الاصطناعي.",
            "items": [
                {
                    "org": "نادي الذكاء الاصطناعي",
                    "role": "التخطيط والتواصل",
                    "date": "سبتمبر 2024 – يونيو 2026",
                    "text": "قيادة مبادرات تعليمية في الذكاء الاصطناعي، منها إعداد محتوى معسكر جامعي واسع النطاق وتقديم ورش عملية في تعلّم الآلة لطلاب المرحلة الثانوية.",
                    "highlight": ("950+", "مشاركًا استفادوا من المبادرات"),
                    "tags": ["القيادة", "إعداد المحتوى", "ورش تعلّم الآلة"],
                },
                {
                    "org": "Google Developer Groups on Campus",
                    "role": "لجنة الأتمتة",
                    "date": "مارس 2026 – يوليو 2026",
                    "text": "إطلاق أداة وكيل ذكي مستقل تقيّم المتقدمين للفعاليات وترتّبهم وفق معايير الأهلية وتقييم التفضيلات ومنطق قرار قائم على القواعد.",
                    "highlight": ("70%", "رفع كفاءة فرز المتقدمين"),
                    "tags": ["الوكلاء الأذكياء", "الأتمتة", "المجتمع التقني"],
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
