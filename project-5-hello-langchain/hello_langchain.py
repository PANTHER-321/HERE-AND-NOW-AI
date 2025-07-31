from langchain_google_genai import chatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
goole_api_key = os.getenv("GOOGLE_API_KEY")
model ="gemini-2.5-flash-lite"

def run_hello_langchain():
    llm = chatGoogleGenerativeAI(model=model, api_key=goole_api_key)
    response = llm.invoke("explain RLHF in 2 lines!")
    print(response.content)

run_hello_langchain()    