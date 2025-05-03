"""
Configurations
"""
import os
from dotenv import dotenv_values, load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI


load_dotenv()
if os.path.exists(".env"):
    config = dotenv_values(".env")
else:
    config = dict(os.environ)
    
class Configs:
    persist_dir = "chroma_db"
    openai_client = ChatOpenAI(model=config['OPENAI_MODEL_NAME'],api_key=config['OPENAI_API_KEY'])
    embedding_model = OpenAIEmbeddings(model=config['OPENAI_EMBEDDING_MODEL_NAME'], api_key=config['OPENAI_API_KEY'])
    
