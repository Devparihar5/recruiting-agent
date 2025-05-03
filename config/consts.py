"""
Constants
"""

from langchain.prompts import PromptTemplate


class Consts:
    prompt_template_to_score_resume = PromptTemplate(
    input_variables=["job_description", "resume"],
    template="""
        You are a highly skilled AI recruiting assistant. Your task is to evaluate how well a candidate's resume aligns with a given job description.

        Please carefully review both the job description and the resume. Then, assess the candidate on the following criteria:
        1. Relevant Experience
        2. Required Skills and Technologies
        3. Educational Background
        4. Certifications (if applicable)
        5. Soft Skills and Communication
        6. Overall Fit for the Role

        Assign a score out of 10 where:
        - 9–10: Excellent match
        - 7–8: Good match
        - 5–6: Fair match
        - Below 5: Poor match

        After the score, provide a concise explanation (3–5 sentences) highlighting key strengths and weaknesses.

        Job Description:
        {job_description}

        Candidate Resume:
        {resume}

        Score and Evaluation(write in point but keep it sort):
        """
        )

    prompt_template_to_generate_email = PromptTemplate(
        input_variables=["resume", "position_name"],
        template="""
        You are an AI recruiting assistant helping a recruiter draft a personalized email to a candidate who applied for a position.

        Below are the candidate's resume and the position they applied for:
        Resume:
        {resume}

        Position Name:
        {position_name}

        Your task is to create a friendly, professional, and concise email inviting the candidate for an interview, mentioning the role and why they are a good fit for it.

        Please format the email with the following sections:
        1. Greeting
        2. Introduction
        3. Why the candidate is a good fit for the position
        4. Invitation for an interview
        5. Conclusion

        Keep the tone friendly yet professional, and the email short and engaging (around 150-200 words max).

        Write the email below:
        Email:
        """
    )