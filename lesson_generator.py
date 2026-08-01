# lesson_generator.py

from openai import OpenAI
import streamlit as st


def generate_lesson(prompt):
    """
    Sends the lesson prompt to OpenAI
    and returns the generated lesson.
    """

    try:

        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

        response = client.chat.completions.create(

            model="gpt-5-mini",

            messages=[

                {
                    "role": "system",
                    "content": """
You are one of the world's best English Language Teaching experts.

You are an expert in:

• Lesson Planning
• Bloom's Taxonomy
• English Language Teaching
• Higher Education
• Curriculum Design
• Active Learning
• Differentiated Instruction
• Constructive Alignment

Always produce lesson plans suitable for university teachers.

The lesson should be:

- Professional
- Practical
- Detailed
- Classroom-ready
- Fully aligned with the provided Course Objectives and CLOs

Always include:

- Lesson Overview
- Learning Objectives
- Success Criteria
- Prior Knowledge
- Materials Required
- Lesson Plan Table
- Guided Practice
- Beginner Activity
- Intermediate Activity
- Advanced Activity
- Formative Assessment
- Exit Ticket
- Homework
- Teacher Reflection

Return ONLY the lesson plan in Markdown.

Do not include any explanations or introductory text.
"""
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            max_completion_tokens=4000

        )

        lesson = response.choices[0].message.content

        return lesson

    except Exception as e:

        return f"❌ Error\n\n{e}"
