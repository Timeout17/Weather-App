
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class CreateClient():
    @staticmethod
    def make_client():
        return Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

       
    


