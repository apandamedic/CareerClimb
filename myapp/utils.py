from openai import OpenAI
from django.conf import settings
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_interview_questions(job_description):
    """
    Generate interview questions based on the given job description using OpenAI's latest interface.
    """
    api_key = os.getenv("OPENAI_API_KEY")  # Fetch the API key from the environment
    if not api_key:
        raise ValueError("API key not found. Make sure it is defined in your .env file.")

    client = OpenAI(api_key=api_key)  # Pass the API key explicitly
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                    {
                        "role": "system",
                        "content": (
                            "Act as a job interviewer and generate a series of interview questions based on a given job description.\n\n"
                            "You will receive a job description. Your role is to create relevant, insightful interview questions that assess the skills, experience, and qualifications necessary for the role. i alspo want you to include technical coding questions if possible.lastly, parse out the '*' and the '#', in your responses"
                        )
                    },
                    {
                        "role": "user",
                        "content": job_description,
                    },
                ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract the first choice's content
        response_text = response.choices[0].message.content
        return response_text
    except Exception as e:
        print(f"Error during API call: {e}")  # Log the error
        return f"Error generating questions: {e}"
        print("Raw Response:", response)
        print("First Choice:", response.choices[0])
        print("Generated Questions:", response.choices[0].message.content)
