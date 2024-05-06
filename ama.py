import streamlit as sl
import json
import requests
import toml  ## Read config file

def read_streamlit_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config_data = toml.load(config_file)
            return config_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    
## Read Config File
config_file_path = 'config.toml'
streamlit_config = read_streamlit_config(config_file_path)
if streamlit_config:
    #print("Streamlit configuration:")
    #print(f"API URL: {streamlit_config.get('api', {}).get('url', 'N/A')}")
    api_url = streamlit_config.get('api', {}).get('url', 'N/A')
    #print(f"Port: {streamlit_config.get('server.port', 'N/A')}")
    # Add other relevant keys as needed
else:
    print("Failed to read Streamlit config file.")


with sl.chat_message("assistant"):
    sl.write("Hi, This is Ginger, your Tender Evaluation Assistant.")

question = sl.chat_input("Say something")
if question:
    with sl.chat_message("User"):
        sl.write(question)

    api_url = api_url
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
