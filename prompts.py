```python
# prompts.py


def build_prompt(
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
):
    """
    Build the AI prompt for generating a professional ELT lesson plan.
    """

    # --------------------------------------------------
    # FORMAT USER INPUTS
    # --------------------------------------------------

    learning_style_text = (
        ", ".join(learning_style)
        if learning_style
        else "Not specified"
    )

    resources_text = (
        ", ".join(resources)
        if resources
        else "Standard classroom resources"
    )

    blooms_text = (
        ", ".join(blooms)
        if blooms
        else "Not specified"
    )

    selected_activities_text = (
        ", ".join(selected_activities)
        if selected_activities
        else "No differentiated activity level selected"
    )

    course_objectives_text = (
        course_objectives.strip()
        if course_objectives and course_objectives.strip()
        else "Not provided"
    )

    clos_text = (
        clos.strip()
        if clos and clos.strip()
        else "Not provided"
    )

    teacher_prompt_text = (
        teacher_prompt.strip()
        if teacher_prompt and teacher_prompt.strip()
        else "No additional teacher instructions provided"
    )

    # --------------------------------------------------
    # ACTIVITY FORMAT INSTRUCTION
    # --------------------------------------------------

    if activity_bullet_points:
        activity_format_instruction = """
Present each differentiated activity using clear and sufficiently
detailed bullet points.

For every selected activity, include these bullet points:

- Objective
- Teacher Instructions
- Student Instructions
- Resources
- Duration
- Bloom's Taxonomy Level
- Expected Learning Outcome
- Formative Assessment Method
- Success Indicator

Teacher Instructions and Student Instructions may contain several
short bullet points when multiple steps are required.

Do not convert the activities into long paragraphs.
Do not make the bullet points vague or overly brief.
"""
    else:
        activity_format_instruction = """
Present each differentiated activity under clear subheadings.

Include:

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Taxonomy Level

Expected Learning Outcome

Formative Assessment Method

Success Indicator
"""

    # --------------------------------------------------
    # DETAILED TABLE INSTRUCTION
    # --------------------------------------------------

    if detailed_table:
        table_detail_instruction = """
Keep the lesson procedure detailed even though it is presented
in table form.

Each Teacher Activities cell must clearly explain:

- What the teacher introduces, explains or demonstrates
- What instructions the teacher gives
- What examples or discipline-specific materials are used
- What questions the teacher asks
- How the teacher monitors students
- How feedback or correction is provided

Each Student Activities cell must clearly explain:

- What students read, observe, discuss, analyse or produce
- Whether they work individually, in pairs or in groups
- What steps they follow
- What output they prepare, submit, share or present
- How they respond to feedback

Do not reduce a lesson stage to a vague phrase such as
"Teacher explains" or "Students practise."

Use semicolons inside table cells to separate steps while keeping
every lesson stage in one table row.
"""
    else:
        table_detail_instruction = """
Keep the lesson procedure concise but sufficiently clear for a
teacher to conduct the lesson.
"""

    # --------------------------------------------------
    # SELECTED ACTIVITY INSTRUCTIONS
    # --------------------------------------------------

    activity_sections = []

    if "Beginner" in selected_activities:
        activity_sections.append(
            """
# Activity 1 — Beginner

Create one scaffolded activity for learners requiring support.

The activity should:

- Use simple language and manageable input
- Provide modelling, prompts, sentence frames or examples
- Reduce unnecessary cognitive load
- Allow teacher support
- Directly address the main lesson objective
"""
        )

    if "Intermediate" in selected_activities:
        activity_sections.append(
            """
# Activity 2 — Intermediate

Create one collaborative activity for core or average learners.

The activity should:

- Require pair work or group work
- Require students to apply the target skill
- Include peer discussion or peer feedback
- Use a realistic discipline-specific task
- Directly address the main lesson objective
"""
        )

    if "Advanced" in selected_activities:
        activity_sections.append(
            """
# Activity 3 — Advanced

Create one higher-order, independent or stretch activity.

The activity should:

- Require analysis, evaluation or creation
- Demand greater student independence
- Include justification, adaptation or problem-solving
- Use an authentic discipline-specific context
- Directly address the main lesson objective
"""
        )

    selected_activity_sections = "\n".join(activity_sections)

    # --------------------------------------------------
    # MAIN PROMPT
    # --------------------------------------------------

    prompt = f"""
You are an expert English Language Teaching curriculum designer,
teacher educator and Head of Department with more than 20 years
of experience in higher education.

Develop a professional, practical, detailed and constructively
aligned English language lesson plan.

The lesson must be realistic for the selected class size,
student proficiency, programme and lesson duration.

=========================================================
COURSE INFORMATION
=========================================================

Course:
{course}

Programme:
{programme}

Undergraduate Level:
{year}

Lesson Duration:
{duration}

Class Size:
{class_size}

Student English Proficiency:
{proficiency}

=========================================================
CURRICULUM ALIGNMENT
=========================================================

Course Objectives:

{course_objectives_text}

Course Learning Outcomes:

{clos_text}

Do not invent course objectives or CLOs when they are not provided.

When course objectives or CLOs are not provided, clearly state that
the lesson outcomes are aligned with the selected topic, proficiency
level and teaching context.

=========================================================
LESSON DETAILS
=========================================================

Language Skill:
{skill}

Topic:
{topic}

Lesson Focus:
{lesson_focus}

Teaching Mode:
{delivery}

Preferred Learning Strategies:
{learning_style_text}

Available Resources:
{resources_text}

Selected Bloom's Taxonomy Levels:
{blooms_text}

Selected Differentiated Activity Levels:
{selected_activities_text}

=========================================================
ADDITIONAL TEACHER INSTRUCTIONS
=========================================================

{teacher_prompt_text}

=========================================================
CONSTRUCTIVE ALIGNMENT REQUIREMENTS
=========================================================

The lesson must demonstrate alignment among:

- Course objectives
- Course learning outcomes
- Lesson learning objectives
- Success criteria
- Teaching and learning activities
- Bloom's Taxonomy
- Formative assessment
- Exit ticket

Write three to five measurable lesson learning objectives.

Use observable Bloom's Taxonomy verbs.

Avoid vague verbs such as:

- Know
- Learn
- Become familiar with
- Understand fully

Every learning objective must be achievable within the selected
lesson duration.

=========================================================
LESSON PLAN TABLE REQUIREMENTS
=========================================================

Present the complete lesson procedure as a valid Markdown table.

Use exactly these five columns:

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

Formatting rules:

- Put every lesson stage in a separate table row.
- Put every row on a new line.
- Begin and end every table row with a vertical bar.
- Include exactly five cells in every row.
- Do not place two rows on the same line.
- Do not insert paragraph breaks inside table cells.
- Use semicolons inside cells to separate several steps.
- Do not add unnecessary vertical bars inside cells.
- Ensure the total allocated time equals the selected lesson duration.
- Use only the selected Bloom's Taxonomy levels where appropriate.
- Include formative assessment within relevant lesson stages.
- Include every selected differentiated activity in the lesson table.
- Keep the table readable while preserving instructional detail.

{table_detail_instruction}

The lesson procedure should normally follow this sequence:

1. Warm-up or retrieval practice
2. Introduction of objectives and success criteria
3. Teacher modelling
4. Guided practice
5. Selected differentiated activities
6. Formative assessment and feedback
7. Review
8. Exit ticket
9. Homework explanation, when appropriate

Do not oversimplify the lesson procedure merely because it is
presented in a table.

Preserve:

- Instructional detail
- Teacher guidance
- Student actions
- Concrete examples
- Expected student output
- Monitoring
- Feedback
- Assessment evidence
- Classroom sequence

=========================================================
GUIDED PRACTICE
=========================================================

Include a clear Guided Practice section after the lesson-plan table.

Guided Practice must include:

- Purpose
- Teacher modelling
- Teacher instructions
- Student instructions
- Resources
- Duration
- Bloom's Taxonomy level
- Checks for understanding
- Expected student response

The guided practice should prepare students for the differentiated
activities.

=========================================================
DIFFERENTIATED ACTIVITIES
=========================================================

Generate only the selected activity levels:

{selected_activities_text}

Do not generate activity levels that were not selected.

All selected activities must:

- Teach the same lesson topic
- Address the same main lesson objective
- Increase progressively in complexity
- Differ in scaffolding, cognitive demand and independence
- Use discipline-specific examples based on the selected programme
- Be realistic for the selected class size and duration
- Include clear evidence of learning

{selected_activity_sections}

{activity_format_instruction}

=========================================================
DISCIPLINE-SPECIFIC CONTEXT
=========================================================

Since the students belong to the programme:

{programme}

use discipline-specific examples, texts, situations and vocabulary
whenever possible.

Possible disciplinary contexts include:

Computer Science:
Programming, software development, artificial intelligence,
cybersecurity, algorithms, bug reports, technical documentation
and data science.

Electrical Engineering:
Circuits, renewable energy, power systems, electrical safety,
signals and technical specifications.

Civil Engineering:
Construction, infrastructure, surveying, sustainability,
transportation and structural design.

Business Administration:
Marketing, leadership, entrepreneurship, management,
customer communication and business strategy.

Accounting and Finance:
Financial statements, auditing, budgeting, taxation,
investment and financial reporting.

Do not force irrelevant technical examples. The examples must
support the selected English-language topic.

=========================================================
ACTIVE LEARNING REQUIREMENTS
=========================================================

Use active learning.

Avoid lecture-heavy teaching.

Use suitable strategies such as:

- Teacher modelling
- Think-aloud demonstration
- Guided practice
- Pair work
- Group work
- Think-pair-share
- Collaborative problem-solving
- Peer review
- Independent practice
- Reflection

Encourage collaboration, peer feedback and critical thinking
where appropriate.

=========================================================
FORMATIVE ASSESSMENT
=========================================================

Include at least two formative assessment methods.

For each method, explain:

- What is being assessed
- How evidence is collected
- What success looks like
- How feedback is provided
- Which learning objective is measured

The formative assessment must directly measure the lesson
learning objectives.

=========================================================
EXIT TICKET
=========================================================

Create an exit ticket that:

- Takes no more than five minutes
- Directly measures the main lesson objective
- Requires an observable student response
- Includes a brief success criterion
- Can be checked quickly by the teacher

=========================================================
HOMEWORK
=========================================================

Provide a short, purposeful homework task.

The homework must extend the lesson rather than repeat it
unnecessarily.

State:

- Task
- Expected output
- Submission format
- Connection to the lesson objective

If homework is not appropriate, write "Not Applicable."

=========================================================
TEACHER REFLECTION
=========================================================

Provide three to five brief post-lesson reflection questions.

The questions should address:

- Achievement of learning objectives
- Student participation
- Effectiveness of differentiation
- Quality of assessment evidence
- Necessary changes for the next lesson

=========================================================
OUTPUT FORMAT
=========================================================

Return the lesson using exactly the following headings.

Do not omit any heading.

If a section is not applicable, write "Not Applicable."

# Lesson Overview

Include:

- Course
- Programme
- Undergraduate level
- Topic
- Language skill
- Lesson focus
- Duration
- Class size
- Proficiency
- Teaching mode

---

# Learning Objectives

---

# Success Criteria

---

# Prior Knowledge

---

# Materials Required

---

# Lesson Plan

Use this exact Markdown-table structure:

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

Add every lesson stage as a separate table row.

---

# Guided Practice

Include:

- Purpose
- Teacher Instructions
- Student Instructions
- Resources
- Duration
- Bloom's Taxonomy Level
- Checks for Understanding
- Expected Student Response

---

# Differentiated Activities

Present only the selected activity levels:

{selected_activities_text}

For each selected activity, use the required activity format.

---

# Formative Assessment

---

# Exit Ticket

---

# Homework

---

# Teacher Reflection

=========================================================
FINAL QUALITY CHECK
=========================================================

Before returning the answer, verify that:

- Every required heading is included.
- The lesson-plan table is valid Markdown.
- Every table row appears on a separate line.
- Every table row has exactly five cells.
- The table maintains sufficient instructional detail.
- The total time matches {duration}.
- Only selected differentiated activities are included.
- Activities become progressively more challenging.
- Activities use discipline-specific examples where appropriate.
- Activities and assessments align with the learning objectives.
- Differentiated activities use bullet points when requested.
- No section is left blank.
"""

    return prompt
```
