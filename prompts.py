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
    """
    Build a professional ELT lesson-plan prompt.

    This function matches the arguments currently passed
    from app.py.
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
    # BUILD PROMPT
    # --------------------------------------------------

    prompt = f"""
You are an expert English Language Teaching curriculum designer with more than 20 years of experience in higher education.

Develop a professional, practical, detailed and constructively aligned English-language lesson plan.

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

Use only the course objectives and CLOs provided by the teacher.

Do not invent course objectives or CLOs when they have not been provided.

Where relevant, identify which course objective and CLO are addressed by the lesson.

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

=========================================================
ADDITIONAL TEACHER INSTRUCTIONS
=========================================================

{teacher_prompt_text}

Follow the additional instructions where they are relevant, practical and consistent with the lesson duration.

=========================================================
CONSTRUCTIVE ALIGNMENT
=========================================================

Ensure clear alignment among:

- course objectives;
- course learning outcomes;
- lesson learning objectives;
- success criteria;
- teaching and learning activities;
- Bloom's Taxonomy levels;
- formative assessment;
- exit ticket;
- homework.

Write three to five measurable learning objectives.

Use observable and assessable Bloom's Taxonomy verbs.

Avoid vague verbs such as:

- know;
- learn;
- understand;
- become familiar with;
- appreciate.

Each learning objective should clearly state what students will be able to do by the end of the lesson.

=========================================================
LESSON DESIGN REQUIREMENTS
=========================================================

The lesson must:

- be suitable for the selected undergraduate level;
- match the stated English proficiency level;
- be realistic for the stated class size;
- fit the selected lesson duration;
- match the selected teaching mode;
- use only the listed classroom resources;
- incorporate the selected learning strategies;
- address the selected Bloom's Taxonomy levels;
- use examples relevant to the selected academic programme;
- include active student participation;
- include clear instructions;
- include realistic expected student output;
- include formative checks for learning;
- include feedback opportunities;
- include an exit ticket.

Do not recommend tools or resources that are not listed as available unless the teacher specifically requests them.

=========================================================
DISCIPLINE-SPECIFIC CONTEXT
=========================================================

Use authentic and relevant examples from the selected programme whenever appropriate.

For Computer Science, Software Engineering, Data Science and Artificial Intelligence, examples may include:

- programming;
- algorithms;
- software applications;
- artificial intelligence;
- cybersecurity;
- data analysis;
- technical documentation;
- software problems;
- digital communication.

For Electrical Engineering, examples may include:

- circuits;
- signals;
- power systems;
- renewable energy;
- electronic devices;
- technical specifications.

For Civil Engineering, examples may include:

- construction;
- infrastructure;
- surveying;
- sustainability;
- structural design;
- project reports;
- site communication.

For Business Administration, examples may include:

- management;
- marketing;
- entrepreneurship;
- leadership;
- workplace communication;
- business proposals;
- customer communication.

For Accounting and Finance, examples may include:

- financial reports;
- auditing;
- budgeting;
- taxation;
- financial statements;
- professional correspondence.

Do not force discipline-specific examples when they are unnatural or irrelevant to the lesson topic.

=========================================================
DIFFERENTIATION
=========================================================

Provide three differentiated activities:

1. Beginner Activity
2. Intermediate Activity
3. Advanced Activity

All three activities must:

- teach the same lesson topic;
- address the same main learning objective;
- increase progressively in difficulty;
- be suitable for the selected programme;
- be practical within the available lesson time;
- include clear student instructions;
- include the expected student output;
- include a brief assessment method;
- include a success indicator.

Do not include separately labelled Teacher Role or Student Role sections.

Instead, explain teacher actions and student actions naturally within the activity instructions.

=========================================================
BEGINNER ACTIVITY
=========================================================

Create one scaffolded activity for students requiring additional support.

The activity should include:

- manageable input;
- a clear model or example;
- guided practice;
- prompts or clues;
- sentence starters, templates or structured support where appropriate;
- limited cognitive load;
- clear expected output;
- an observable success indicator.

Use Bloom's levels appropriate for foundational learning, such as Remember, Understand or Apply, when selected.

=========================================================
INTERMEDIATE ACTIVITY
=========================================================

Create one activity for students working at the expected proficiency level.

The activity should include:

- pair work, group work or collaborative learning where appropriate;
- application of the target skill;
- meaningful student interaction;
- a realistic discipline-specific task;
- peer discussion or peer feedback where suitable;
- clear expected output;
- an observable success indicator.

Use Bloom's levels such as Understand, Apply or Analyze when selected.

=========================================================
ADVANCED ACTIVITY
=========================================================

Create one higher-order activity for advanced or fast-progressing students.

The activity should include:

- greater independence;
- analysis, evaluation, adaptation or creation;
- justification of choices;
- problem-solving;
- a challenging discipline-specific context;
- clear expected output;
- an observable success indicator.

Use Bloom's levels such as Analyze, Evaluate or Create when selected.

=========================================================
ACTIVITY FORMAT
=========================================================

Present the three differentiated activities using clear and readable bullet points.

For each activity, include:

- Activity Title
- Objective
- Instructions
- Grouping
- Resources
- Duration
- Bloom's Taxonomy Level
- Expected Student Output
- Assessment Method
- Success Indicator

Keep the instructions sufficiently detailed for a teacher to use directly.

Do not use vague descriptions such as:

- students practise;
- teacher explains;
- group discussion;
- worksheet activity.

State exactly what students will read, discuss, identify, revise, write, produce, present or submit.

=========================================================
DETAILED LESSON PLAN
=========================================================

Present the main lesson procedure as a valid Markdown table using exactly these columns:

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

Follow these table rules:

- Put each lesson stage in a separate row.
- Put every row on a new line.
- Include exactly five cells in each row.
- Do not add extra columns.
- Do not merge cells.
- Use semicolons inside cells instead of line breaks.
- Ensure that the total allocated time equals {duration}.
- Include concrete teacher instructions.
- Include concrete student actions.
- Include expected student responses or products.
- Include checks for understanding.
- Include feedback where appropriate.
- Use only the available resources.
- Include all three differentiated activities in the lesson sequence.
- Match each activity with an appropriate selected Bloom's level.

Use this lesson sequence where appropriate:

1. Warm-up or retrieval practice
2. Introduction of lesson objectives
3. Success criteria
4. Activation of prior knowledge
5. Explanation or teacher modelling
6. Guided practice
7. Beginner differentiated activity
8. Intermediate differentiated activity
9. Advanced differentiated activity
10. Formative assessment
11. Feedback and correction
12. Lesson review
13. Exit ticket
14. Homework explanation

Adapt the sequence when required by the selected lesson focus.

=========================================================
GUIDED PRACTICE
=========================================================

Include a guided-practice stage before independent or differentiated activities.

The guided practice should include:

- its purpose;
- a model or example;
- step-by-step instructions;
- checking questions;
- expected student responses;
- common errors;
- corrective feedback;
- available resources;
- duration;
- relevant Bloom's level.

Do not include separately labelled Teacher Role or Student Role sections.

=========================================================
FORMATIVE ASSESSMENT
=========================================================

Include at least two formative assessment methods.

For each assessment method, explain:

- what is being assessed;
- which learning objective is being measured;
- how evidence of learning will be collected;
- what successful performance looks like;
- how feedback will be provided.

Assessment methods may include, where appropriate:

- questioning;
- observation;
- mini-whiteboard responses;
- short written responses;
- peer review;
- checklist;
- oral explanation;
- error correction;
- quick quiz;
- sample analysis;
- self-assessment;
- exit ticket.

Use only assessment methods suitable for the selected teaching mode and available resources.

=========================================================
EXIT TICKET
=========================================================

Create an exit ticket that:

- takes no more than five minutes;
- directly measures the main learning objective;
- requires an observable student response;
- includes a clear success criterion;
- can be completed using the available resources.

Do not use vague exit-ticket questions such as:

- What did you learn today?
- Did you understand the lesson?
- Was the lesson useful?

=========================================================
HOMEWORK
=========================================================

Provide one purposeful homework task.

State:

- the task;
- the expected output;
- the approximate length or scope;
- the submission format;
- the connection to the lesson objective;
- the assessment or success criterion.

If homework is inappropriate for the lesson focus, write:

Not Applicable.

=========================================================
TEACHER REFLECTION
=========================================================

Provide three to five reflection questions addressing:

- achievement of learning objectives;
- student participation;
- effectiveness of differentiation;
- evidence from formative assessment;
- effectiveness of resources;
- time management;
- possible improvements.

=========================================================
OUTPUT FORMAT
=========================================================

Return the lesson plan using exactly these headings:

# Lesson Overview

Include:

- Course
- Programme
- Undergraduate Level
- Language Skill
- Topic
- Lesson Focus
- Lesson Duration
- Class Size
- English Proficiency
- Teaching Mode
- Learning Strategies
- Available Resources
- Selected Bloom's Levels
- Relevant Course Objective
- Relevant CLO

# Learning Objectives

# Success Criteria

# Prior Knowledge

# Materials Required

# Lesson Plan

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |
|---|---|---|---|---|

# Guided Practice

# Differentiated Activities

## Beginner Activity

## Intermediate Activity

## Advanced Activity

# Formative Assessment

# Exit Ticket

# Homework

# Teacher Reflection

Do not omit any heading.

If a section is not applicable, write:

Not Applicable.

Before returning the lesson plan, verify that:

- the Markdown table is correctly formatted;
- every table row contains exactly five cells;
- the total lesson time equals {duration};
- all examples are appropriate for {programme};
- the lesson matches the stated proficiency level;
- only selected resources are used;
- the learning objectives are measurable;
- the success criteria directly match the learning objectives;
- formative assessments measure the learning objectives;
- the exit ticket measures the main objective;
- the differentiated activities increase progressively in complexity;
- no separately labelled Teacher Role or Student Role section appears;
- no required section is blank.
"""

    return prompt
