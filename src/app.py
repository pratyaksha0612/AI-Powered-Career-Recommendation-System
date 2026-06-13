import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from recommender import CareerRecommender

st.set_page_config(
    page_title="CareerAI",
    layout="wide"
)
st.markdown("""
<style>
.stApp{
    background:#081120;
}
div[data-testid="stVerticalBlock"]{
    gap:0.5rem;
}
.hero{
    background:linear-gradient(135deg,#172554,#0f172a);
    padding:1.2rem 1.5rem;
    border-radius:18px;
    margin-bottom:1rem;
    border:1px solid #334155;
}
.hero h1{
    font-size:34px;
    font-weight:700;
}
.category-title{
    font-size:18px;
    font-weight:600;
    margin-top:20px;
    margin-bottom:10px;
    color: white;
}
.badge-row{
    margin-bottom:15px;
}
[data-testid="stMetric"]{
    background:#111827;
    border:1px solid #334155;
    padding:15px;
    border-radius:15px;
}
.card{
    background:#111827;
    border:1px solid #334155;
    border-radius:18px;
    padding:18px;
    margin-bottom:15px;
}
.role{
    font-size:24px;
    font-weight:700;
    color:white;
    margin-bottom:8px;
}
.match{
    color:#22c55e;
    font-size:22px;
    font-weight:700;
}
.section{
    color:#94a3b8;
    font-weight:600;
    margin-top:12px;
}
.badge{
    display:inline-block;
    background:#172554;
    color:#e2e8f0;
    padding:5px 12px;
    border-radius:999px;
    margin:4px;
    font-size:14px;
    border:1px solid #2563eb;
}
div[class*="st-key-search_box"]{
    background:#0f172a;
    border:1px solid #334155;
    border-radius:18px;
    padding:20px 22px;
    margin-bottom:20px;
}
.search-label{
    font-size:13px;
    font-weight:600;
    letter-spacing:0.05em;
    text-transform:uppercase;
    color:#94a3b8;
    margin-bottom:8px;
    margin-top:4px;
}
div[data-testid="stMultiSelect"] > div > div{
    background:#111827;
    border-radius:12px;
    border:1px solid #334155;
}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"]{
    background-color:#2563eb;
    border-radius:999px;
}
div.stButton > button[kind="primary"]{
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    color:white;
    border:none;
    border-radius:999px;
    font-weight:600;
    height:40px;
    font-size:14px;
    transition:all 0.2s ease;
}
div.stButton > button[kind="primary"]:hover{
    background:linear-gradient(135deg,#1d4ed8,#1e40af);
    border:none;
    color:white;
}
div[class*="st-key-search_box"] div.stButton > button[kind="primary"]{
    border-radius:12px;
    height:44px;
    font-size:15px;
}
div[class*="st-key-catpanel_"]{
    border:1px solid #334155;
    border-radius:16px;
    padding:28px 20px 20px 20px;
    margin-top:18px;
    margin-bottom:12px;
    position:relative;
    background:#0a1322;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
}
div[class*="st-key-catpanel_"] .category-panel-title{
    position:absolute;
    top:-13px;
    left:20px;
    background:#081120;
    padding:0 12px;
    font-size:17px;
    font-weight:700;
    color:white;
    letter-spacing:0.02em;
    line-height:1.4;
    border:1px solid #334155;
    border-radius:8px;
}
div.stButton > button[kind="secondary"]{
    background:#1e2937;
    color:#e2e8f0;
    border:1px solid #475569;
    border-radius:9999px;
    font-weight:500;
    font-size:13.5px;
    min-height:40px;
    padding:8px 18px;
    white-space:normal !important;
    line-height:1.2;
}
div.stButton > button[kind="secondary"]:hover{
    background:#334155;
    border-color:#60a5fa;
    color:white;
    transform: translateY(-1px);
}
div[class*="st-key-chipgrid_"]{
    margin-top:12px;
}
div[class*="st-key-chipgrid_"] [data-testid="stVerticalBlock"]{
    display:flex !important;
    flex-wrap:wrap !important;
    flex-direction:row !important;
    gap:10px !important;
}
div.stButton > button[kind="primary"]{
    min-height:40px;
    padding:8px 18px;
    white-space:normal !important;
    line-height:1.2;
}
div[class*="st-key-catrow_"] div[data-testid="stHorizontalBlock"]{
    gap: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

DATA_PATH = Path(__file__).parent.parent / "data" / "jobs.csv"

recommender = CareerRecommender(DATA_PATH)

all_skills = sorted({
    skill.strip()
    for skills in recommender.df["Skills"]
    for skill in skills.split(",")
})

skill_categories = {
    "AI / ML": [
        "AI","Machine Learning","Deep Learning","NLP",
        "TensorFlow","Transformers","OpenCV",
        "MLflow","Research"
    ],

    "Programming": [
        "Python","Java","C","C++","C#","JavaScript",
        "Dart","Kotlin","Swift","SQL"
    ],

    "Web Development": [
        "HTML","CSS","React","Node.js","Django",
        "Flask","REST API","APIs","Git"
    ],

    "Cloud & DevOps": [
        "AWS","Azure","GCP","Docker",
        "Kubernetes","Linux","Terraform",
        "CI/CD","Monitoring"
    ],

    "Data & Analytics": [
        "Pandas","Excel","Power BI","Analytics",
        "Statistics","Spark","Hadoop",
        "Kafka","ETL","Data Visualization"
    ],

    "Cyber Security": [
        "Security","Ethical Hacking",
        "Penetration Testing","Networking",
        "Cisco"
    ],

    "Design": [
        "Figma","Photoshop","Illustrator",
        "Canva","Wireframing","Prototyping",
        "UX","UI"
    ],

    "Mobile": [
        "Flutter","Firebase",
        "Android Studio","Xcode"
    ],

    "Business": [
        "Agile","Scrum","Leadership",
        "Communication","Product Management",
        "Financial Modeling","Recruitment"
    ]
}
st.markdown("""
<div class="hero">
<h1 style="margin:0;font-size:38px;">
CareerAI
</h1>
<p style="margin-top:8px;">
AI-powered career matching using skill analysis
</p>
</div>
""", unsafe_allow_html=True)

if "selected_skills" not in st.session_state:
    st.session_state.selected_skills = []

if "ms_key_version" not in st.session_state:
    st.session_state.ms_key_version = 0

def toggle_skill(skill):
    if skill in st.session_state.selected_skills:
        st.session_state.selected_skills.remove(skill)
    else:
        st.session_state.selected_skills.append(skill)
    st.session_state.ms_key_version += 1

def sync_from_multiselect():
    ms_key = f"skills_multiselect_{st.session_state.ms_key_version}"
    st.session_state.selected_skills = list(st.session_state[ms_key])

search_box = st.container(key="search_box")

with search_box:
    st.markdown(
        "<div class='category-title' style='margin-top:0;'>Select Your Skills</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([5, 1])

    with col1:
        ms_key = f"skills_multiselect_{st.session_state.ms_key_version}"

        st.multiselect(
            "Skills",
            all_skills,
            default=st.session_state.selected_skills,
            placeholder="Search and add skills...",
            label_visibility="collapsed",
            key=ms_key,
            on_change=sync_from_multiselect
        )

    with col2:
        search = st.button(
            "Find Careers",
            use_container_width=True,
            type="primary"
        )

    if st.session_state.selected_skills:
        st.markdown(
            f"<div style='color:#94a3b8;font-size:13px;margin-top:8px;'>"
            f"{len(st.session_state.selected_skills)} skill(s) selected"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='color:#64748b;font-size:13px;margin-top:8px;'>"
            "No skills selected yet — pick some below or use the search box above."
            "</div>",
            unsafe_allow_html=True
        )

st.markdown(
    "<div class='search-label'>Browse by Category</div>",
    unsafe_allow_html=True
)

categories_list = []

for category, skills in skill_categories.items():
    available = [s for s in skills if s in all_skills]
    if available:
        categories_list.append((category, available))

n_cols = 3
for row_idx in range(0, len(categories_list), n_cols):
    row_categories = categories_list[row_idx:row_idx + n_cols]

    with st.container(key=f"catrow_{row_idx}"):
        cols = st.columns(n_cols)

        for col, (category, available) in zip(cols, row_categories):
            with col:
                with st.container(key=f"catpanel_{category}"):
                    st.markdown(
                        f"<div class='category-panel-title'>{category}</div>",
                        unsafe_allow_html=True
                    )

                    with st.container(key=f"chipgrid_{category}"):
                        cols_per_row =3
                        for i in range(0, len(available), cols_per_row):
                            row_skills = available[i:i + cols_per_row]
                            cols = st.columns(cols_per_row)
                            for col_idx, skill in enumerate(row_skills):
                                with cols[col_idx]:
                                    is_selected = skill in st.session_state.selected_skills
                                    if st.button(
                                        skill,
                                        key=f"chip_{category}_{skill}",
                                        type="primary" if is_selected else "secondary",
                                        use_container_width=True
                                    ):
                                        toggle_skill(skill)
                                        st.rerun()

selected_skills = st.session_state.selected_skills

if search:
    if not selected_skills:
        st.warning("Select at least one skill.")
        st.stop()

    results = recommender.recommend(selected_skills, min_score=0.0)

    st.markdown("<div id='results-section'></div>", unsafe_allow_html=True)

    st.markdown("## Insights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Top Match",
            f"{results.iloc[0]['Match %']}%"
        )

    with c2:
        st.metric(
            "Skills Selected",
            len(selected_skills)
        )

    with c3:
        st.metric(
            "Recommendations",
            len(results)
        )

    st.markdown("---")

    st.markdown("## Career Recommendations")

    cols = st.columns(3)

    for i, (_, row) in enumerate(results.iterrows()):

        matched_html = "".join(
            [
                f"<span class='badge'>{s}</span>"
                for s in row["Matched Skills"]
            ]
        )

        missing_html = "".join(
            [
                f"<span class='badge'>{s}</span>"
                for s in row["Missing Skills"]
            ]
        )

        with cols[i % 3]:

            st.markdown(f"""
            <div class="card">

            <div class="role">
            {row['Role']}
            </div>

            <div class="match">
            {row['Match %']}% Match
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.progress(
                min(row["Match %"] / 100, 1.0)
            )

            st.markdown("**Matched Skills**")

            st.markdown(
                matched_html if matched_html else "None",
                unsafe_allow_html=True
            )

            st.markdown("**Skills To Learn**")

            st.markdown(
                missing_html if missing_html else "None",
                unsafe_allow_html=True
            )
    components.html("""
    <script>
        var el = window.parent.document.getElementById('results-section');
        if (el) {
            el.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    </script>
    """, height=0)