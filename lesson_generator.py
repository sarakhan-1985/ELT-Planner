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

            model="gpt-5",

            messages=[

                {
                    "role": "system",
                    "content":
                    """
You are one of the world's best English Language Teaching experts.

You are an expert in

• Lesson Planning
• Bloom's Taxonomy
• English Language Teaching
• Higher Education
• Curriculum Design
• Active Learning
• Differentiated Instruction
• Constructive Alignment

Always produce lessons suitable for university teachers.

The lesson should be professional, practical, detailed and classroom ready.

Do NOT give explanations.

Return ONLY the lesson plan.
                    """
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.7,

            max_completion_tokens=4000

        )

        lesson = response.choices[0].message.content

        return lesson

    except Exception as e:

        return f"❌ Error\n\n{e}"