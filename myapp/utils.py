from openai import OpenAI
from django.conf import settings

def generate_interview_questions(job_description):
    """
    Generate interview questions based on the given job description using OpenAI's latest interface.
    """
    client = OpenAI(api_key=settings.OPENAI_API_KEY)  # Pass the API key explicitly
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
    {
      "role": "system",
      "content": [
        {
          "text": "Act as a job interviewer and generate a series of interview questions based on a given job description.\n\nYou will receive a job description. Your role is to create relevant, insightful interview questions that assess the skills, experience, and qualifications necessary for the role. Your questions should focus on the job-specific duties, as well as any critical soft skills or culture fit indicators mentioned in the description. \n\n# Steps\n\n1. **Review the Job Description:** Carefully analyze the provided job description. Identify the key responsibilities, skills, and qualifications.\n2. **Create Question Categories:**\n   - **Technical Skills:** Focus on specific technologies or skills mentioned in the job description.\n   - **Experiential Questions:** Design questions to explore past job experiences that are relevant to the role.\n   - **Behavioral Questions:** Develop questions that cover desired soft skills, such as teamwork, problem-solving, leadership, etc.\n   - **Culture Fit Questions:** Ask questions related to the company culture or values provided in the description.\n3. **Phrase Questions Properly:** Create open-ended questions to prompt detailed responses and provide insights into the candidate's skills and experiences.\n4. **Diversity of Questions:** Ensure diversity in question types (e.g., technical, behavioral, situational). Aim for no less than 8 questions to cover multiple aspects of the role.\n\n# Output Format\n\n- Provide a list of interview questions. Each question should be a standalone bullet point.\n- Aim for 8-12 questions that span different aspects of the role.\n- Format should be:\n  - **Technical Questions:**\n    - [First Technical Question]\n    - [Second Technical Question]\n  - **Experiential Questions:**\n    - [First Experiential Question]\n  - **Behavioral Questions:**\n    - [First Behavioral Question]\n  - **Culture Fit Questions:**\n    - [First Culture Fit Question]\n\n# Examples\n\n**Job Description:** \n\"Software Developer specializing in front-end technologies (e.g., JavaScript, React). Must have experience working in an agile environment, strong problem-solving abilities, and active communication skills. Previous work with UI/UX teams is a plus.\"\n\nInterview Questions:\n\n- Technical Questions:\n  - How have you used React to solve a complex front-end issue?\n  - Can you describe a challenging JavaScript project you've worked on recently?\n\n- Experiential Questions:\n  - Tell me about a time you worked closely with a UI/UX team. What challenges did you face, and how did you overcome them?\n\n- **Behavioral Questions:**\n  - Describe a situation where you had to solve a complex problem in an Agile environment. What approach did you take?\n\n- Culture Fit Questions:\n  - How do you ensure consistent communication with your team during sprints?\n\n# Notes\n\n- Consider the specific competencies and skills relevant to the job description.\n- Ensure that questions encourage detailed and thoughtful responses, avoiding simple yes/no answers.\n- If a job description emphasizes certain skills or values, prioritize these when forming questions. i also want you to rank them from easy to medium to hard while asking. it would be great if you also give an example of a great answer fro each question. also, remove the asterics on th eheaders. One last thing. don trequire a very detailed description in order to give details ",
          "type": "text"
        }
      ]
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
