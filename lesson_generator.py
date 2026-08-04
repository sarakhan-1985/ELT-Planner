from openai import OpenAI
import streamlit as st


def generate_lesson(prompt):

    try:
        api_key = st.secrets.get("OPENAI_API_KEY")

        if not api_key:
            return "❌ OPENAI_API_KEY is missing from Streamlit Secrets."

        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5-mini",
            instructions="""
You are an expert English Language Teaching curriculum designer.

Create a professional, practical, classroom-ready university
English lesson plan.

Follow the structure and instructions supplied by the user.

Return only the lesson plan in Markdown.
""",
            input=prompt,
            max_output_tokens=6000
        )

        lesson = response.output_text

        if not lesson:
            return "❌ OpenAI returned an empty lesson plan."

        return lesson

    except Exception as e:
        return f"❌ Lesson generation failed:\n\n{str(e)}"
