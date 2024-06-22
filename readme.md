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


# Git Chek out and Check in

```
git pull origin main
or 
git pull --rebase

--adding new file
git add <file name>
--commit
git commit -m 'remakr'

-- to add or stage all the files including new folder
git add .

--push to Github. below is in the main branch
git push origin main
```

Edit existing file and commit. example this README.md

```
git add README.md
git commit -m "my changes"
git push origin main
```
