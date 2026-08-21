
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

       
"""    
from groq import Groq

client = Groq()

models = client.models.list()

for model in models.data:
    print(model.id)

"""