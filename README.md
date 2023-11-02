
###Проект выполненный в рамках проектных семинаров, являющийся лендингом с информацией о себе


# How to use project?



## Getting started


Create .env file and setup your environment variables


CODEWARS_USER_NAME = "your codewars user name"
...
GITHUB_USER_NAME = "your github user name"
...
GITHUB_ACCESS_TOKEN = "your github Access token"
...

Look how to get your github Access token [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)!


Don't foget to install requirements!

```
pip install -r requirements.txt

```

## Launching

You have to be sure you have python3 installed!

For launching Python Virtual Environment on Windows machine

```
python -m venv venv
source venv/Scripts/activate
```

For launching programm

```
cd "project path"
py main.py

```
## Output

If everything was done correctly you will find out new directory called "data". Inside "data" directory lay two new json files. First one contain your codewars account information, second one contain your github account information. They called codewars.json and github.json correspondly.
