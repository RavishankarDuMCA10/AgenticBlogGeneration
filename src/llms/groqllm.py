from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


class GroqLLM:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

        os.environ["GROQ_API_KEY"] = api_key

    def get_llm(self):
        try:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(api_key=self.groq_api_key, model="llama-3.3-70b-versatile")
            return llm
        except Exception as e:
            raise ValueError("Error occured with exception: {e}")
