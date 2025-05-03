from langchain.chains import LLMChain
from config.configs import Configs
from config.consts import Consts


class EmailGenerator:
    @staticmethod
    def generate(resume: str, position_name: str) -> str:
        """
        Generate an email using the resume and position name.
        """
        email_chain = Consts.prompt_template_to_generate_email | Configs.openai_client
        input_data = {
            'resume': resume,
            'position_name': position_name
        }
        return email_chain.invoke(input_data).content
