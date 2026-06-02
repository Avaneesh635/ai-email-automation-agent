import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def classify_email(email):

    prompt = f"""
Classify this email.

Categories:
- Customer Support
- Complaint
- Sales
- Meeting Request
- Job Application
- General Inquiry

Return only category.

Email:
{email}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()


def analyze_priority(email):

    prompt = f"""
Determine priority.

Options:
- Low
- Medium
- High
- Critical

Return only priority.

Email:
{email}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()


def summarize_email(email):

    prompt = f"""
Summarize this email in 2-3 lines.

Email:
{email}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()


def extract_actions(email):

    prompt = f"""
Extract action items.

Return bullet points only.

Email:
{email}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()


def generate_reply(email):

    prompt = f"""
Write a professional email reply.

Email:
{email}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()