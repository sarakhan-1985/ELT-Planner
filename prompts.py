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

    learning_style_text = ", ".join(learning_style) if learning_style else "Not Specified"

    resources_text = ", ".join(resources) if resources else "Standard Classroom Resources"

    blooms_text = ", ".join(blooms)

    prompt = f"""

You are an expert English Language Teaching (ELT) curriculum designer with more than 20 years of experience in higher education.

Develop a PROFESSIONAL lesson plan.

-------------------------------------------------------
COURSE INFORMATION
-------------------------------------------------------

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

-------------------------------------------------------
CURRICULUM ALIGNMENT
-------------------------------------------------------

Course Objectives

{course_objectives}

-------------------------------------------------------

Course Learning Outcomes (CLOs)

{clos}

-------------------------------------------------------
LESSON DETAILS
-------------------------------------------------------

Language Skill:
{skill}

Topic:
{topic}
-------------------------------------------------------
DIFFERENTIATED ACTIVITIES
-------------------------------------------------------

For the topic "{topic}", generate ALL of the following:

🟢 Beginner Activity

Create one easy activity suitable for struggling learners.

Include:

- Objective
- Teacher Instructions
- Student Instructions
- Resources
- Time
- Bloom's Level

-------------------------------------------------------

🟡 Intermediate Activity

Create one collaborative activity for average learners.

Include:

- Objective
- Teacher Instructions
- Student Instructions
- Resources
- Time
- Bloom's Level

-------------------------------------------------------

🔴 Advanced Activity

Create one higher-order thinking activity.

Include:

- Objective
- Teacher Instructions
- Student Instructions
- Resources
- Time
- Bloom's Level

-------------------------------------------------------

All three activities MUST teach the SAME lesson topic.

The activities should increase in difficulty.

Never omit any activity.
Lesson Focus:
{lesson_focus}

Teaching Mode:
{delivery}

Preferred Learning Strategy:
{learning_style_text}

Available Resources:
{resources_text}

Bloom's Taxonomy Levels

{blooms_text}

-------------------------------------------------------
ADDITIONAL TEACHER INSTRUCTIONS
-------------------------------------------------------

{teacher_prompt}

-------------------------------------------------------
IMPORTANT INSTRUCTIONS
-------------------------------------------------------

Design the lesson professionally.

The lesson MUST include:

1. Lesson Overview

2. Learning Objectives
   - Aligned with Bloom's Taxonomy
   - Aligned with Course Objectives
   - Aligned with CLOs

3. Success Criteria

4. Prior Knowledge

5. Materials Required

6. Lesson Plan Table

The table should have

Time

Teacher Activities

Student Activities

Resources

Bloom's Level

=========================================================
DIFFERENTIATED LEARNING ACTIVITIES (COMPULSORY)
=========================================================

The lesson MUST contain ALL FOUR sections below.

Do NOT omit any section.

---------------------------------------------------------
Guided Practice (Teacher Modelling)
---------------------------------------------------------

Duration

Teacher Instructions

Student Instructions

Resources Required

Bloom's Taxonomy Level

---------------------------------------------------------
Activity 1 – Beginner
---------------------------------------------------------

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Taxonomy Level

Expected Learning Outcome

---------------------------------------------------------
Activity 2 – Intermediate
---------------------------------------------------------

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Taxonomy Level

Expected Learning Outcome

---------------------------------------------------------
Activity 3 – Advanced
---------------------------------------------------------

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Taxonomy Level

Expected Learning Outcome

---------------------------------------------------------

All activities should become progressively more difficult.

Activity 1 should target low proficiency learners.

Activity 2 should target average learners.

Activity 3 should target high-achieving learners.

Use discipline-specific examples based on the selected programme.


The activities should progressively increase in difficulty.

10. Formative Assessment

11. Exit Ticket

12. Homework

13. Teacher Reflection

-------------------------------------------------------
VERY IMPORTANT
-------------------------------------------------------

Since the students belong to

{programme}

all examples, activities and texts should be discipline-specific whenever possible.

Examples

Computer Science

Artificial Intelligence

Programming

Cyber Security

Data Science

Electrical Engineering

Renewable Energy

Circuits

Power Systems

Business Administration

Marketing

Leadership

Entrepreneurship

Accounting & Finance

Financial Statements

Auditing

Budgeting

Civil Engineering

Construction

Infrastructure

Sustainability

-------------------------------------------------------

Use active learning.

Avoid lecture-heavy teaching.

Every lesson should follow the sequence:

Teacher Modelling

↓

Guided Practice

↓

Activity 1 (Support)

↓

Activity 2 (Collaborative)

↓

Activity 3 (Independent Challenge)

↓

Exit Ticket

Every activity must clearly state:

• Objective

• Teacher Instructions

• Student Instructions

• Time Required

• Resources

• Bloom's Level

• Expected Learning Outcome

The activities should naturally progress from easier to more challenging tasks.

Encourage collaboration, peer feedback, and critical thinking where appropriate.

Return the lesson using EXACTLY the following format.

Do NOT omit any heading.

If a section is empty, write "Not Applicable".

# Lesson Overview

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

| Time | Teacher Activities | Student Activities | Resources | Bloom's Level |

---

# Guided Practice

Teacher Instructions

Student Instructions

Resources

Time

---

# Activity 1 (Beginner)

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Level

Expected Learning Outcome

---

# Activity 2 (Intermediate)

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Level

Expected Learning Outcome

---

# Activity 3 (Advanced)

Objective

Teacher Instructions

Student Instructions

Resources

Duration

Bloom's Level

Expected Learning Outcome

---

# Formative Assessment

---

# Exit Ticket

---

# Homework

---

# Teacher Reflection

Generate ALL sections.

"""

    return prompt
