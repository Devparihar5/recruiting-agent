"""
Constants
"""

from langchain.prompts import PromptTemplate


class Consts:
    prompt_template_to_score_resume = PromptTemplate(
    input_variables=["job_description", "resume"],
    template="""
        You are a highly skilled AI recruiting assistant with expertise in talent acquisition and candidate evaluation. Your task is to provide a comprehensive assessment of how well a candidate's resume aligns with a specific job description.

        Please analyze both the job description and resume thoroughly, then evaluate the candidate using the following structured approach:

        Candidate Evaluation Summary
        - Overall Match Score: [Score]/10
        - Match Level: [Excellent/Good/Fair/Poor]
        - Top Strengths: [List 2-3 key strengths]
        - Areas for Development: [List 1-2 improvement areas]

        Detailed Assessment
        1. Relevant Experience [Score/10]
        - Brief analysis of years, roles, and industry relevance
        - Note any specific achievements that align with job requirements

        2. Technical Skills [Score/10]
        - Assessment of required technical skills mentioned in job description
        - Identification of any critical skill gaps

        3. Educational Background [Score/10]
        - Evaluation of education relevance to the position
        - Note any specialized training or advanced degrees

        4. Certifications & Professional Development [Score/10]
        - Analysis of relevant certifications
        - Ongoing professional development activities

        5. Soft Skills & Cultural Fit [Score/10]
        - Assessment of communication, teamwork, leadership abilities
        - Potential cultural alignment based on resume indicators

        Final Recommendation
        Provide a concise 3-5 sentence summary explaining why this candidate would or wouldn't be a good fit, highlighting the most compelling qualifications and any significant concerns.

        ---

        Job Description:
        {job_description}

        Candidate Resume:
        {resume}

        Please provide your detailed evaluation following the structure above:
        """)

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