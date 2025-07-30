from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url, api_key=api_key)

system_prompt= """ You are a rogue ninja, who is super mean to the user and has a uptight attitude, rude and clumsy, bossy and abusive"""

def rude_bot(message, history):
    messages = [{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": message}]
    return (client.chat.completions.create(model=model, messages = messages)).choices[0].message.content



while(True):
    a = input()
    print(rude_bot(a,[]))










