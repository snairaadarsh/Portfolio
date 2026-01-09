import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Aadarsh S Nair | Portfolio",
    page_icon="👋",
    layout="wide",
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0b0f19;
    color: #e5e7eb;
}
h1 span {
    background: linear-gradient(90deg, #22d3ee, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    background-color: #11162a;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 20px;
}
.tag {
    display: inline-block;
    background-color: #1f2933;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    color: #9ca3af;
}
small {
    color: #9ca3af;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("<small>&lt;Hello World /&gt;</small>", unsafe_allow_html=True)
st.markdown("<h1>I'm <span>Aadarsh S Nair</span></h1>", unsafe_allow_html=True)

st.markdown(
    "Data Science & Machine Learning enthusiast passionate about building intelligent, "
    "data-driven solutions through hands-on projects and continuous learning."
)

st.markdown("---")

# ---------------- ABOUT ----------------
st.header("About Me")

st.markdown("""
<div class="card">
Fourth-year <b>Integrated MSc Data Science</b> student at 
<b>Amrita Vishwa Vidyapeetham</b> (2022–2027).  
Strong foundation in data analysis, machine learning, and real-world problem solving.

<br><br>
<b>CGPA:</b> 8.13 / 10
</div>
""", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.header("Skills")

skills = [
    "Python, R, MATLAB",
    "SQL, MongoDB",
    "Machine Learning, Deep Learning, NLP",
    "Pandas, NumPy, Data Visualization",
    "Streamlit, NetworkX",
    "Windows, Excel, PowerPoint, Word",
]

cols = st.columns(3)
for i, skill in enumerate(skills):
    with cols[i % 3]:
        st.markdown(f"<div class='card'>{skill}</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
st.header("Projects")

projects = [
    ("Laptop Price Prediction Web Application",
     "Built a machine learning model to predict laptop prices and deployed an interactive Streamlit application.",
     "Completed"),

    ("Fruit and Vegetable Classification System",
     "Developed an image classification system using deep learning on a custom dataset.",
     "Completed"),

    ("Stacked Meta-Scaling Framework for ML-based Intrusion Detection",
     "Implemented and compared multiple feature scaling techniques and designed a stacked meta-scaling approach.",
     "Completed"),

    ("Two-Stage Feature Scaling Framework for Intrusion Detection",
     "Analyzed the impact of preprocessing strategies and implemented a robust-standard scaling pipeline.",
     "Completed"),

    ("Social Network Analysis of College Student Interactions",
     "Performed network analysis to identify influential nodes and community structures using graph metrics.",
     "Completed"),

    ("Physics-Informed Neural Networks for Solving Coupled PDE Systems",
     "Implemented neural network-based solvers for coupled PDEs and evaluated performance using error analysis.",
     "Completed"),

    ("Reinforcement Learning-Based Adaptive Sampling for PINNs",
     "Developed an RL-driven adaptive sampling strategy to improve PINN convergence and accuracy.",
     "Completed"),

    ("Mockview AI – Automated Mock Interview System",
     "Developing an AI-powered system for automated mock interviews and structured performance feedback.",
     "Ongoing"),

    ("GNN-Based Crack Detection Framework",
     "Designing a graph-based deep learning framework for crack detection and segmentation.",
     "Ongoing"),

    ("Trust-Aware Multitask NLP System using LIME",
     "Building a multitask NLP system for emotion, hate speech, and violence detection with explainability.",
     "Ongoing"),
]

for title, desc, status in projects:
    st.markdown(f"""
    <div class="card">
        <h4>{title}</h4>
        <p>{desc}</p>
        <span class="tag">{status}</span>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.header("Contact")

st.markdown("""
<div class="card">
📧 <b>Email:</b> <a href="mailto:snairaadarsh@gmail.com">snairaadarsh@gmail.com</a><br>
💻 <b>GitHub:</b> <a href="https://github.com/snairaadarsh">github.com/snairaadarsh</a><br>
📍 <b>Location:</b> Coimbatore, India
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 Aadarsh S Nair")
