import streamlit as st
import json
from prompts import build_prompt
from lesson_generator import generate_lesson
from pathlib import Path


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ELT Planner AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #F8FAFC;
    }

    h1 {
        color: #003366;
        font-weight: 700;
    }

    h2 {
        color: #004B8D;
    }

    .section-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .stButton > button {
        background-color: #003366;
        color: white;
        border-radius: 10px;
        height: 55px;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #00509E;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/graduation-cap.png",
    width=80
)

st.sidebar.markdown("## ELT Planner AI")

st.sidebar.info(
    """
    Use this application to generate professionally structured,
    differentiated and Bloom's Taxonomy-based English language
    lesson plans.
    """
)


# --------------------------------------------------
# HOME PAGE HEADER
# --------------------------------------------------

st.title("🎓 ELT Planner AI")

st.markdown(
    """
    ### Professional Lesson Planning Assistant for English Language Teachers

    Design engaging, Bloom's Taxonomy-based lesson plans in minutes.

    Upload your course outline or enter your course objectives and CLOs,
    select your programme, choose your lesson topic, and let AI generate
    a professional lesson plan.
    """
)

st.divider()


# --------------------------------------------------
# STEP 1 — COURSE INFORMATION
# --------------------------------------------------

st.markdown("## 📘 Step 1 — Course Information")

col1, col2 = st.columns(2)

with col1:

    course = st.selectbox(
        "Course Title",
        [
            "Functional English",
            "Expository Writing",
            "English I",
            "Technical Business Writing",
            "Communication Skills",
            "Presentation Skills"
        ]
    )

    programme = st.selectbox(
        "Programme",
        [
            "Computer Science",
            "Software Engineering",
            "Data Science",
            "Artificial Intelligence",
            "Electrical Engineering",
            "Civil Engineering",
            "Business Administration",
            "Accounting & Finance"
        ]
    )

    year = st.selectbox(
        "Undergraduate Level",
        [
            "First Year",
            "Second Year",
            "Third Year",
            "Fourth Year",
            "Fifth Year"
        ]
    )

with col2:

    duration = st.selectbox(
        "Lesson Duration",
        [
            "40 Minutes",
            "60 Minutes",
            "90 Minutes",
            "110 Minutes"
        ]
    )

    class_size = st.number_input(
        "Class Size",
        min_value=5,
        max_value=150,
        value=30,
        step=1
    )

    proficiency = st.selectbox(
        "Student English Proficiency",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
            "Mixed Ability"
        ]
    )

st.divider()


# --------------------------------------------------
# STEP 2 — CURRICULUM ALIGNMENT
# --------------------------------------------------

st.markdown("## 📄 Step 2 — Curriculum Alignment")

uploaded_file = st.file_uploader(
    "Upload Course Outline",
    type=["pdf", "docx"],
    help="Upload a PDF or DOCX course outline."
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

st.markdown("### OR")

course_objectives = st.text_area(
    "Paste Course Objectives",
    height=180,
    placeholder="""
Example:

CO1: Develop academic reading skills.

CO2: Develop effective academic writing skills.

CO3: Develop professional communication skills.
"""
)

clos = st.text_area(
    "Paste Course Learning Outcomes",
    height=180,
    placeholder="""
Example:

CLO1: Identify the main features of effective academic writing.

CLO2: Apply appropriate writing strategies in academic tasks.

CLO3: Evaluate written texts for clarity, organisation and accuracy.
"""
)

st.divider()


# --------------------------------------------------
# STEP 3 — LESSON DETAILS
# --------------------------------------------------

st.markdown("## 📝 Step 3 — Lesson Details")

topics = {
    "Writing": [
        "Paraphrasing",
        "Summary Writing",
        "Expository Writing",
        "Narrative Writing",
        "Descriptive Writing",
        "Compare and Contrast Essay",
        "Cause and Effect Essay",
        "Persuasive Essay",
        "Email Writing",
        "Report Writing",
        "Technical Writing"
    ],

    "Reading": [
        "Stated Main Idea",
        "Implied Main Idea",
        "Supporting Details",
        "Critical Response Questions",
        "Inference",
        "Fact vs Opinion",
        "Author's Purpose",
        "Tone",
        "Vocabulary in Context"
    ],

    "Listening": [
        "Listening for Gist",
        "Listening for Details",
        "Lecture Comprehension",
        "Note Taking",
        "TED Talk Analysis"
    ],

    "Speaking": [
        "Presentation Skills",
        "Group Discussion",
        "Debate",
        "Interview Skills",
        "Extempore Speaking"
    ],

    "Grammar": [
        "Parts of Speech",
        "Sentence Structure",
        "Subject-Verb Agreement",
        "Tenses",
        "Active and Passive Voice",
        "Direct and Indirect Speech",
        "Clauses",
        "Punctuation"
    ]
}

col1, col2 = st.columns(2)

with col1:

    skill = st.selectbox(
        "Language Skill",
        list(topics.keys())
    )

    lesson_focus = st.selectbox(
        "Lesson Focus",
        [
            "Teaching New Concept",
            "Revision",
            "Practice",
            "Exam Preparation",
            "Assessment",
            "Project Lesson"
        ]
    )

with col2:

    topic = st.selectbox(
        "Lesson Topic",
        topics[skill]
    )

# --------------------------------------------------
# ACTIVITY OPTIONS
# --------------------------------------------------

st.markdown("### 🎯 Activities to Generate")

activity_col1, activity_col2 = st.columns(2)

with activity_col1:

    beginner_activity = st.checkbox(
        "🟢 Beginner Activity",
        value=True
    )

    intermediate_activity = st.checkbox(
        "🟡 Intermediate Activity",
        value=True
    )

    advanced_activity = st.checkbox(
        "🔴 Advanced Activity",
        value=True
    )

with activity_col2:

    activity_bullet_points = st.checkbox(
        "• Present activities in bullet points",
        value=True,
        help=(
            "The AI will present each activity using short, "
            "clear and readable bullet points."
        )
    )

selected_activities = []

if beginner_activity:
    selected_activities.append("Beginner")

if intermediate_activity:
    selected_activities.append("Intermediate")

if advanced_activity:
    selected_activities.append("Advanced")

st.divider()


# --------------------------------------------------
# STEP 4 — TEACHING CONTEXT
# --------------------------------------------------

st.markdown("## 👨‍🏫 Step 4 — Teaching Context")

col1, col2 = st.columns(2)

with col1:

    delivery = st.selectbox(
        "Teaching Mode",
        [
            "Face-to-Face",
            "Online",
            "Hybrid"
        ]
    )

with col2:

    learning_style = st.multiselect(
        "Preferred Learning Strategies",
        [
            "Individual Learning",
            "Pair Work",
            "Group Work",
            "Collaborative Learning",
            "Think-Pair-Share",
            "Problem-Based Learning",
            "Inquiry-Based Learning",
            "Peer Teaching",
            "Task-Based Learning"
        ],
        default=[
            "Individual Learning",
            "Pair Work",
            "Group Work"
        ]
    )

resources = st.multiselect(
    "Available Resources",
    [
        "Projector",
        "Internet",
        "Whiteboard",
        "Printed Handouts",
        "AI Tools",
        "Smart Classroom",
        "Student Mobile Phones",
        "Learning Management System"
    ],
    default=[
        "Projector",
        "Whiteboard",
        "Printed Handouts"
    ]
)

st.divider()


# --------------------------------------------------
# STEP 5 — BLOOM'S TAXONOMY
# --------------------------------------------------

st.markdown("## 🎯 Step 5 — Bloom's Taxonomy")

st.caption(
    "Select the cognitive levels you want the lesson to target."
)

blooms = st.multiselect(
    "Bloom's Levels",
    [
        "Remember",
        "Understand",
        "Apply",
        "Analyze",
        "Evaluate",
        "Create"
    ],
    default=[
        "Remember",
        "Understand",
        "Apply",
        "Analyze",
        "Evaluate",
        "Create"
    ]
)

st.divider()


# --------------------------------------------------
# STEP 6 — AI TEACHING INSTRUCTIONS
# --------------------------------------------------

st.markdown("## 🤖 Step 6 — AI Teaching Instructions")

teacher_prompt = st.text_area(
    "Additional Instructions Optional",
    height=220,
    placeholder="""
Example:

Develop an interactive lesson.

Use authentic examples from Computer Science.

Include retrieval practice.

Include collaborative learning.

Add formative assessment.

Add an exit ticket.

Ensure constructive alignment between objectives,
activities and assessment.
"""
)


# --------------------------------------------------
# PROMPT QUALITY
# --------------------------------------------------

word_count = len(teacher_prompt.split())

if word_count == 0:
    st.error("Prompt Quality: Not Provided")

elif word_count < 10:
    st.warning("🟥 Prompt Quality: Basic")

elif word_count < 35:
    st.info("🟨 Prompt Quality: Good")

else:
    st.success("🟩 Prompt Quality: Excellent")

st.divider()
generate = st.button(
    "🚀 Generate Professional Lesson Plan",
    use_container_width=True
)

if generate:

    with st.spinner("Generating your lesson..."):

        prompt = build_prompt(

            course,
            programme,
            year,
            duration,
            class_size,
            proficiency,
            course_objectives,
            clos,
            skill,
            topic,
            lesson_focus,
            delivery,
            learning_style,
            resources,
            blooms,
            teacher_prompt

        )

        lesson = generate_lesson(prompt)

        st.success("Lesson Generated Successfully!")

        st.markdown("---")

        st.markdown(lesson)

