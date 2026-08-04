import streamlit as st

from prompts import build_prompt
from lesson_generator import generate_lesson


def normalize_lesson_text(result):
    """Convert common AI response formats into displayable lesson text."""
    if result is None:
        return ""

    if isinstance(result, str):
        return result.strip()

    if isinstance(result, dict):
        for key in ("output_text", "text", "content", "lesson", "response"):
            value = result.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()

        choices = result.get("choices")
        if isinstance(choices, list) and choices:
            first = choices[0]
            if isinstance(first, dict):
                message = first.get("message", {})
                if isinstance(message, dict):
                    content = message.get("content")
                    if isinstance(content, str) and content.strip():
                        return content.strip()
                text_value = first.get("text")
                if isinstance(text_value, str) and text_value.strip():
                    return text_value.strip()

    output_text = getattr(result, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    choices = getattr(result, "choices", None)
    if choices:
        first = choices[0]
        message = getattr(first, "message", None)
        content = getattr(message, "content", None) if message else None
        if isinstance(content, str) and content.strip():
            return content.strip()

        text_value = getattr(first, "text", None)
        if isinstance(text_value, str) and text_value.strip():
            return text_value.strip()

    fallback = str(result).strip()
    return fallback if fallback and fallback != "None" else ""


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

    custom_topic = st.text_input(
        "Custom Topic Optional",
        placeholder="Enter a topic not listed above"
    )

final_topic = custom_topic.strip() if custom_topic.strip() else topic


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

    include_teacher_role = st.checkbox(
        "Include teacher role",
        value=True
    )

    include_student_role = st.checkbox(
        "Include student role",
        value=True
    )

    include_activity_assessment = st.checkbox(
        "Include assessment for each activity",
        value=True
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


# --------------------------------------------------
# GENERATE LESSON PLAN
# --------------------------------------------------

generate = st.button(
    "🚀 Generate Professional Lesson Plan",
    use_container_width=True
)

if generate:
    validation_errors = []

    if not blooms:
        validation_errors.append(
            "Please select at least one Bloom's Taxonomy level."
        )

    if not selected_activities:
        validation_errors.append(
            "Please select at least one activity level."
        )

    if validation_errors:
        for error in validation_errors:
            st.error(error)
    else:
        with st.spinner("Generating your professional lesson plan..."):
            try:
                prompt = build_prompt(
                    course=course,
                    programme=programme,
                    year=year,
                    duration=duration,
                    class_size=class_size,
                    proficiency=proficiency,
                    course_objectives=course_objectives,
                    clos=clos,
                    skill=skill,
                    topic=final_topic,
                    lesson_focus=lesson_focus,
                    delivery=delivery,
                    learning_style=learning_style,
                    resources=resources,
                    blooms=blooms,
                    teacher_prompt=teacher_prompt,
                    selected_activities=selected_activities,
                    activity_bullet_points=activity_bullet_points,
                    include_teacher_role=include_teacher_role,
                    include_student_role=include_student_role,
                    include_activity_assessment=include_activity_assessment
                )

                raw_lesson = generate_lesson(prompt)
                lesson = normalize_lesson_text(raw_lesson)

                if not lesson:
                    raise ValueError(
                        "The AI returned an empty response. Check your API key, "
                        "model settings, and lesson_generator.py."
                    )

                st.session_state["generated_lesson"] = lesson
                st.success("Lesson generated successfully!")

            except Exception as error:
                st.error(
                    "The lesson plan could not be generated. "
                    f"Error: {error}"
                )


# --------------------------------------------------
# DISPLAY GENERATED LESSON
# --------------------------------------------------

if "generated_lesson" in st.session_state:
    lesson = normalize_lesson_text(
        st.session_state.get("generated_lesson")
    )

    if lesson:
        st.markdown("---")
        st.markdown("## 📚 Generated Lesson Plan")
        st.markdown(lesson)

