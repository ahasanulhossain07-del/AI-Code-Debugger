from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
my_api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=my_api_key)

def code_generator(images,options):
    if options=="Hints":
        promt="Analyze these coding error screenshots and give only hints to fix the problem."
    else:
        promt="Analyze these coding error screenshots and provide the correct code with explanation."
    response=client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[images,promt]
    )
    return response.text

