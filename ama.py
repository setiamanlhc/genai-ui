import streamlit as sl
import json
import requests

with sl.chat_message("assistant"):
    sl.write("Hi, This is Ginger, your Tender Evaluation Assistant.")

question = sl.chat_input("Say something")
if question:
    with sl.chat_message("User"):
        sl.write(question)

    api_url = "https://eadawlpffl.execute-api.us-west-2.amazonaws.com/dev/tender-evaluation"
    prompt = { "prompt" : question }
    header = {"Content-Type": "text/plain"}
    response = requests.post(api_url, json=prompt, headers=header)
    if response.status_code == 200:
        answer = json.loads(response.text)
        #sl.write(response.textresponse.text)
        print(answer)
        with sl.chat_message("ai"):
            sl.markdown(answer["body"])

    else:   
        sl.write("Failed to call API")
    ##answer = {
    ##    "statusCode": 200,
    ##    "body": " Hi! My name is Coral, an AI-assistant chatbot trained to assist human users by providing thorough responses. I am powered by Cohere, and would love to help you with whatever you need.  Would you like to know more about Cohere, or have some questions you want to ask me?  "
     ##   }