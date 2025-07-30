from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts import ai_motivational_speaker

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model ="gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = OpenAI(api_key=api_key, base_url=base_url)

ai_motivational_speaker = ai_motivational_speaker


def get_response(message, history):
    messages = [{"role": "system", "content": ai_motivational_speaker}] 
    messages.extend(history)
    messages.append({"role": "user", "content": message})
    response  = client.chat.completions.create(
        model=model,
        messages=messages
    )
    Ai_response = response.choices[0].message.content
    return Ai_response

#if __name__ == "__main__":
   
   # print(get_response("Hello, Caramel AI! Can you tell me what AI is?", []))