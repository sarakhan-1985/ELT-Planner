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

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

h1 {
    color:#003366;
    font-weight:700;
}

h2 {
    color:#004B8D;
}

.section-box{
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.stButton>button{
    background-color:#003366;
    color:white;
    border-radius:10px;
    height:55px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#00509E;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/graduation-cap.png",
    width=80
)

st.sidebar.title("ELT Planner AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📚 Generate Lesson",
        "ℹ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
**Version 1.0**

Developed for English Language Teachers

Features

✔ Bloom's Taxonomy

✔ AI Lesson Planning

✔ CLO Alignment

✔ Differentiated Activities

✔ Prompt Engineering
"""
)

# --------------------------------------------------
# HOME PAGE HEADER
# --------------------------------------------------

st.title("🎓 ELT Planner AI")

st.markdown("""
### Professional Lesson Planning Assistant for English Language Teachers

Design engaging, Bloom's Taxonomy-based lesson plans in minutes.

Upload your Course Outline or enter your Course Objectives and CLOs,
select your programme, choose your lesson topic, and let AI generate
a professional lesson plan.
""")

st.divider()
# --------------------------------------------------
# STEP 1
# COURSE INFORMATION
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
            "Fourth Year"
            "Fifth Year"
        ]
    )

with col2:

    duration = st.selectbox(
        "Lesson Duration",
        [
            "40 Minutes",
            "60 Minutes",
            "90 Minutes"
            "110 Minutes"
        ]
    )

    class_size = st.number_input(
        "Class Size",
        min_value=5,
        max_value=150,
        value=30
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
# STEP 2
# CURRICULUM ALIGNMENT
# --------------------------------------------------

st.markdown("## 📄 Step 2 — Curriculum Alignment")

uploaded_file = st.file_uploader(
    "Upload Course Outline (PDF or DOCX)",
    type=["pdf", "docx"]
)

st.markdown("### OR")

course_objectives = st.text_area(
    "Paste Course Objectives",
    height=180,
    placeholder="""
Example

CO1:
Develop academic reading skills.

CO2:
Develop effective academic writing.

CO3:
Develop communication skills.
"""
)

clos = st.text_area(
    "Paste Course Learning Outcomes (CLOs)",
    height=180,
    placeholder="""
Example

CLO1

CLO2

CLO3
"""
)

st.divider()
# --------------------------------------------------
# STEP 3
# LESSON DETAILS
# --------------------------------------------------

st.markdown("## 📝 Step 3 — Lesson Details")

topics = {

    "Writing":[
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

    "Reading":[
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

    "Listening":[
        "Listening for Gist",
        "Listening for Details",
        "Lecture Comprehension",
        "Note Taking",
        "TED Talk Analysis"
    ],

    "Speaking":[
        "Presentation Skills",
        "Group Discussion",
        "Debate",
        "Interview Skills",
        "Extempore Speaking"
    ]

}

col1,col2 = st.columns(2)

with col1:

    skill = st.selectbox(
        "Language Skill",
        list(topics.keys())
    )

with col2:

    topic = st.selectbox(
        "Lesson Topic",
        topics[skill]
    )

    st.markdown("### Activities to Generate")

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

st.divider()
# --------------------------------------------------
# STEP 4
# TEACHING CONTEXT
# --------------------------------------------------

st.markdown("## 👨‍🏫 Step 4 — Teaching Context")

col1,col2 = st.columns(2)

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

        "Preferred Learning Strategy",

        [

            "Individual Learning",

            "Pair Work",

            "Group Work",

            "Collaborative Learning",

            "Think-Pair-Share",

            "Problem-Based Learning",

            "Inquiry-Based Learning"

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

        "Smart Classroom"

    ]

)

st.divider()
# --------------------------------------------------
# STEP 5
# BLOOM'S TAXONOMY
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
# STEP 6
# AI PROMPT
# --------------------------------------------------

st.markdown("## 🤖 Step 6 — AI Teaching Instructions")

teacher_prompt = st.text_area(

    "Additional Instructions (Optional)",

    height=220,

    placeholder="""
Example

Develop an interactive lesson.

Include collaborative learning.

Use authentic Computer Science examples.

Include formative assessment.

Add an exit ticket.

Provide three differentiated activities.

Align everything with Bloom's Taxonomy.

"""

)
# --------------------------------------------------
# PROMPT QUALITY
# --------------------------------------------------

word_count = len(teacher_prompt.split())

if word_count == 0:

    st.error("Prompt Quality : Not Provided")

elif word_count < 10:

    st.warning("🟥 Prompt Quality : Basic")

elif word_count < 35:

    st.info("🟨 Prompt Quality : Good")

else:

    st.success("🟩 Prompt Quality : Excellent")
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
