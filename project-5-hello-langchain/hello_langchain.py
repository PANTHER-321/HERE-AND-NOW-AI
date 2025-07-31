from langchain_google_genai import chatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
goole_api_key = os.getenv("GOOGLE_API_KEY")
