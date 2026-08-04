import streamlit as st

from prompts import build_prompt
from lesson_generator import generate_lesson


# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def normalize_lesson_text(lesson):
    """Return lesson content as a reliable plain-text string."""
    if lesson is None:
        return ""

    if isinstance(lesson, str):
        return lesson.strip()

    if isinstance(lesson, dict):
        for key in ("content", "text", "lesson", "output_text", "response"):
            value = lesson.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()

        choices = lesson.get("choices")
        if isinstance(choices, list) and choices:
            first = choices[0]
            if isinstance(first, dict):
                message = first.get("message", {})
                if isinstance(message, dict):
                    content = message.get("content")
                    if isinstance(content, str):
                        return content.strip()

    output_text = getattr(lesson, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    choices = getattr(lesson, "choices", None)
    if choices:
        first = choices[0]
        message = getattr(first, "message", None)
        content = getattr(message, "content", None)
        if isinstance(content, str):
            return content.strip()

    return str(lesson).strip()


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
        min-height: 55px;
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
# HOME PAGE HEADER
# --------------------------------------------------

st.title("🎓 ELT Planner AI")

st.markdown(
    """
    ### Professional Lesson Planning Assistant for English Language Teachers

    Design engaging, Bloom's Taxonomy-based lesson plans in minutes.

    Upload your Course Outline or enter your Course Objectives and CLOs,
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
# STEP 2 — CURRICULUM ALIGNMENT
# --------------------------------------------------

st.markdown("## 📄 Step 2 — Curriculum Alignment")

uploaded_file = st.file_uploader(
    "Upload Course Outline (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    st.success(
        f"File uploaded successfully: {uploaded_file.name}"
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

CLO1:
Identify important features of academic texts.

CLO2:
Apply appropriate language strategies.

CLO3:
Evaluate written communication for clarity and accuracy.
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
    ]
}

col1, col2 = st.columns(2)

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


# --------------------------------------------------
# ACTIVITIES TO GENERATE
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
        "• Present differentiated activities in bullet points",
        value=True,
        help=(
            "Each differentiated activity will be shown using "
            "clear but sufficiently detailed bullet points."
        )
    )

    detailed_table = st.checkbox(
        "📋 Keep lesson procedure detailed in table form",
        value=True,
        help=(
            "Teacher actions, student actions, resources and "
            "assessment instructions will remain detailed."
        )
    )


selected_activities = []

if beginner_activity:
    selected_activities.append("Beginner")

if intermediate_activity:
    selected_activities.append("Intermediate")

if advanced_activity:
    selected_activities.append("Advanced")


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
# STEP 6 — AI PROMPT
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
    if not selected_activities:
        st.error(
            "Please select at least one activity level."
        )

    elif not blooms:
        st.error(
            "Please select at least one Bloom's Taxonomy level."
        )

    else:
        with st.spinner(
            "Generating your professional lesson plan..."
        ):
            try:
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
                    teacher_prompt,
                    selected_activities,
                    activity_bullet_points,
                    detailed_table
                )

                raw_lesson = generate_lesson(prompt)
                lesson = normalize_lesson_text(raw_lesson)

                if not lesson:
                    raise ValueError("The AI returned an empty lesson plan.")

                st.session_state["generated_lesson"] = lesson

                st.success(
                    "Lesson Generated Successfully!"
                )

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
        st.session_state["generated_lesson"]
    )

    if not lesson:
        st.error("No lesson-plan content is available to display.")
        st.stop()

    st.markdown("---")
    st.markdown("## 📚 Generated Lesson Plan")
    st.markdown(lesson)
