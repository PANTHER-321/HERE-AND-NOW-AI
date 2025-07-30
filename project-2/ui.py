#import certain libraies
import gradio as gr
from chatbot_with_memory import get_response 
import json 
import os

#using the json file
with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"branding.json"))) as file:
    brand_info = json.load(file)["brand"]
    
#using the gradio lib
with gr.Blocks(theme="default",title=brand_info["organizationName"]) as app:
    gr.HTML(f"""
            <div style="display: flex; justify-content:center; margin-bottom:20px">
            <img src="{brand_info["logo"]["title"]}" alt="{brand_info["organizationName"]} Logo" style ="width:200px;height:40px">
            </div> """)
    
    #creation of chatbot
    gr.ChatInterface (
         fn = get_response,
    chatbot = gr.Chatbot(height=400 ,avatar_images=(None,brand_info["chatbot"]["avatar"]),
                         type = "messages"),
    title = brand_info["organizationName"],
    description= brand_info["slogan"],
    type = "messages",
    examples=[
        ["Who are you!"],
        ["What is the role of ML in AI?"],
        ["What is you favorite choice of ice-cream flavor"]
    ]
        
    )
if __name__ == "__main__":
        app.launch()
   