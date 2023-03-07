import json
from os import environ, mkdir
from requests import get


CODEWARS_USER_NAME = environ.get('CODEWARS_USER_NAME')
GITHUB_USER_NAME = environ.get('GITHUB_USER_NAME')
GITHUB_ACCESS_TOKEN = environ.get('GITHUB_ACCESS_TOKEN')

mkdir("data")

cw_resp = get(
                f"https://www.codewars.com/api/v1/users/{CODEWARS_USER_NAME}",
                timeout=10)
with open('data/codewars.json', 'w', encoding="utf-8") as f:
    json.dump(cw_resp.json(), f, indent=4)

gh_resp = get(
                f"https://api.github.com/users/{GITHUB_USER_NAME}",
                timeout=10,
                headers={
                    'Accept': 'application/vnd.github+json',
                    'Authorization': GITHUB_ACCESS_TOKEN,
                    'X-GitHub-Api-Version': '2022-11-28'
                }
)
with open('data/github.json', 'w', encoding="utf-8") as f:
    json.dump(gh_resp.json(), f, indent=4)
