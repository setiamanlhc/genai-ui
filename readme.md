# Readme First
AMA stand for Ask Me Anything. It is chat bot UI which utilize AWS Bedrock marketplace model. The UI is developed using Sreamlit framework.
This project is for POC purpose.

To run ama.py you need to create config.toml file. Below are the content of config.toml.

```
[api]
url = "Your API URL"
```

To launch Streamlit

```
streamlit run ama.py --server.port 8080
```



