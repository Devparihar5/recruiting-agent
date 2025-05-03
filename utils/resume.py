import re
import nltk
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords


class ResumePreprocessor:
    stopwords_english = set(stopwords.words("english"))

    @staticmethod
    def preprocess_resume(row):
        """
        Combines candidate information into a structured text block.
        """
        return (
            f"career_objective: {row.get('career_objective', '')}\n"
            f"skills: {row.get('skills', '')}\n"
            f"experience: {row.get('positions', '')} at {row.get('professional_company_names', '')} "
            f"{row.get('responsibilities', '')}\n"
            f"education: {row.get('degree_names', '')} from {row.get('educational_institution_name', '')} "
            f"with major {row.get('major_field_of_studies', '')}"
        )

    @staticmethod
    def preprocess_text(text):
        """
        Cleans and tokenizes raw text:
        - Converts to lowercase
        - Removes punctuation and extra whitespace
        - Splits on commas
        - Removes stopwords
        """
        if not isinstance(text, str):
            text = str(text)

        # Normalize and clean text
        clean_text = text.lower()
        clean_text = re.sub(r'[.;|%\[\]()\r\n*]+', '', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_text = re.sub(r'\s-\s', ' ', clean_text)

        # Tokenize and remove stopwords
        tokens = [token.strip() for token in clean_text.split(',')]
        filtered_tokens = [token for token in tokens if token and token not in ResumePreprocessor.stopwords_english]

        return filtered_tokens
