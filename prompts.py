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
    teacher_prompt
):
    """Build a detailed prompt for generating a professional ELT lesson plan."""
    # Default activity settings
    # These are defined here because app.py does not pass them to build_prompt().
    selected_activities = ["Beginner", "Intermediate", "Advanced"]

    # Present activities in bullet points
    activity_bullet_points = True

    # Include teacher and student roles
    include_teacher_role = True
    include_student_role = True

    # Include assessment for each activity
    include_activity_assessment = True
    learning_style_text = (
        ", ".join(learning_style) if learning_style else "Not specified"
    )
    resources_text = (
        ", ".join(resources) if resources else "Standard classroom resources"
    )
    blooms_text = ", ".join(blooms) if blooms else "Not specified"
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
        clos.strip() if clos and clos.strip() else "Not provided"
    )
    teacher_prompt_text = (
        teacher_prompt.strip()
        if teacher_prompt and teacher_prompt.strip()
        else "No additional teacher instructions provided"
    )

    if activity_bullet_points:
        activity_format_instruction = """
Present each differentiated activity using clear, sufficiently detailed bullet points.
Do not reduce instructions to vague phrases or one-line descriptions.
"""
    else:
        activity_format_instruction = """
Present each differentiated activity under clear subheadings with sufficient detail.
"""

    if include_teacher_role:
        teacher_role_instruction = """
For Guided Practice and every selected differentiated activity, include a clearly labelled **Teacher Role**.
Explain what the teacher introduces, models, instructs, monitors, asks, and how feedback or correction is provided.
"""
    else:
        teacher_role_instruction = """
A separately labelled Teacher Role is not required.
"""

    if include_student_role:
        student_role_instruction = """
For Guided Practice and every selected differentiated activity, include a clearly labelled **Student Role**.
Explain what students do, how they are grouped, what steps they follow, what they produce, and how they respond to feedback.
"""
    else:
        student_role_instruction = """
A separately labelled Student Role is not required.
"""

    if include_activity_assessment:
        assessment_instruction = """
For Guided Practice and every selected differentiated activity, include a clearly labelled **Assessment** section stating:
- what is assessed;
- how evidence is collected;
- the success indicator;
- how feedback is provided;
- which learning objective is measured.
"""
    else:
        assessment_instruction = """
Activity-level assessment may be omitted; retain the main Formative Assessment section.
"""

    activity_sections = []

    if "Beginner" in selected_activities:
        activity_sections.append("""
### Activity 1 — Beginner
Create one scaffolded activity for learners requiring support. Use manageable input, examples, prompts, sentence frames, and teacher support. It must address the main lesson objective.
""")

    if "Intermediate" in selected_activities:
        activity_sections.append("""
### Activity 2 — Intermediate
Create one collaborative activity for core learners. Use pair or group work, application of the target skill, peer discussion or feedback, and a realistic discipline-specific task.
""")

    if "Advanced" in selected_activities:
        activity_sections.append("""
### Activity 3 — Advanced
Create one higher-order, independent or stretch activity. Require analysis, evaluation or creation, greater independence, justification, adaptation or problem-solving.
""")

    selected_activity_sections = "\n".join(activity_sections)

    prompt = f"""
You are an expert English Language Teaching curriculum designer, teacher educator and Head of Department with more than 20 years of experience in higher education.

Develop a professional, practical, detailed and constructively aligned English language lesson plan.

=========================================================
COURSE INFORMATION
=========================================================

Course: {course}
Programme: {programme}
Undergraduate Level: {year}
Lesson Duration: {duration}
Class Size: {class_size}
Student English Proficiency: {proficiency}

=========================================================
CURRICULUM ALIGNMENT
=========================================================

Course Objectives:
{course_objectives_text}

Course Learning Outcomes:
{clos_text}

Do not invent course objectives or CLOs when they are not provided.

=========================================================
LESSON DETAILS
=========================================================

Language Skill: {skill}
Topic: {topic}
Lesson Focus: {lesson_focus}
Teaching Mode: {delivery}
Preferred Learning Strategies: {learning_style_text}
Available Resources: {resources_text}
Selected Bloom's Taxonomy Levels: {blooms_text}
Selected Differentiated Activity Levels: {selected_activities_text}

=========================================================
ADDITIONAL TEACHER INSTRUCTIONS
=========================================================

{teacher_prompt_text}

=========================================================
CONSTRUCTIVE ALIGNMENT
=========================================================

Align course objectives, CLOs, lesson objectives, success criteria, teaching activities, Bloom's levels, formative assessment and the exit ticket.
Write three to five measurable learning objectives using observable Bloom's verbs. Avoid vague verbs such as know, learn, or become familiar with.

=========================================================
DETAILED LESSON PLAN TABLE
=========================================================

Present the complete lesson procedure as a valid Markdown table using exactly these columns:

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

Table rules:
- Put each lesson stage in a separate row and each row on a new line.
- Include exactly five cells in every row.
- Keep the table detailed enough for a teacher to conduct the lesson directly from it.
- In Teacher Activities, explain what is introduced, modelled, instructed, questioned, monitored and corrected.
- In Student Activities, explain what students read, discuss, practise, produce, submit, share or present.
- Use semicolons inside cells to preserve detail without creating extra rows.
- Keep concrete examples, expected output, monitoring, feedback and assessment evidence.
- Ensure the total time equals {duration}.
- Include all selected differentiated activities in the table.

Follow this sequence where appropriate:
Warm-up → Objectives and Success Criteria → Teacher Modelling → Guided Practice → Selected Differentiated Activities → Formative Assessment and Feedback → Review → Exit Ticket → Homework Explanation.

=========================================================
GUIDED PRACTICE
=========================================================

Include purpose, modelling, teacher instructions, student instructions, resources, duration, Bloom's level, checks for understanding and expected student response.

{teacher_role_instruction}

{student_role_instruction}

{assessment_instruction}

=========================================================
DIFFERENTIATED ACTIVITIES
=========================================================

Generate only these selected activity levels:
{selected_activities_text}

All selected activities must teach the same lesson topic and main objective while increasing progressively in complexity, cognitive demand and independence.
Use discipline-specific examples suitable for {programme}.

{selected_activity_sections}

{activity_format_instruction}

For every selected activity, include as applicable:
- Objective
- Teacher Role
- Student Role
- Teacher Instructions
- Student Instructions
- Resources
- Duration
- Bloom's Taxonomy Level
- Expected Learning Outcome
- Assessment Method
- Success Indicator

{teacher_role_instruction}

{student_role_instruction}

{assessment_instruction}

=========================================================
DISCIPLINE-SPECIFIC CONTEXT
=========================================================

Use relevant examples from the selected programme whenever possible:
- Computer Science, Software Engineering, Data Science or AI: programming, software development, algorithms, bug reports, cybersecurity, data and technical documentation.
- Electrical Engineering: circuits, renewable energy, power systems, signals and technical specifications.
- Civil Engineering: construction, infrastructure, surveying, sustainability and structural design.
- Business Administration: marketing, leadership, entrepreneurship, management and business communication.
- Accounting & Finance: financial statements, auditing, budgeting, taxation and financial reporting.

Do not force irrelevant technical examples.

=========================================================
ASSESSMENT AND REFLECTION
=========================================================

Include at least two formative assessment methods. Explain what is assessed, how evidence is collected, what success looks like, how feedback is provided, and which objective is measured.

Create an exit ticket taking no more than five minutes that directly measures the main objective and includes a clear success criterion.

Provide a purposeful homework task with expected output, submission format and connection to the lesson objective. If inappropriate, write "Not Applicable."

Provide three to five teacher-reflection questions addressing objectives, participation, differentiation, assessment evidence and improvements.

=========================================================
OUTPUT FORMAT
=========================================================

Return the lesson using exactly these headings:

# Lesson Overview

# Learning Objectives

# Success Criteria

# Prior Knowledge

# Materials Required

# Lesson Plan

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

# Guided Practice

# Differentiated Activities

# Formative Assessment

# Exit Ticket

# Homework

# Teacher Reflection

Do not omit headings. If a section is not applicable, write "Not Applicable."
Before returning the answer, verify that the table is valid Markdown, every row has exactly five cells, total time matches {duration}, only selected activities appear, roles and assessment follow the user's selected options, and no section is blank.
"""

    return prompt
