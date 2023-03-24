"""Module for learning how to use api"""
import json
from os import environ, mkdir, path
from requests import get
from jinja2 import Template


CODEWARS_USER_NAME = environ.get('CODEWARS_USER_NAME')
GITHUB_USER_NAME = environ.get('GITHUB_USER_NAME')
GITHUB_ACCESS_TOKEN = environ.get('GITHUB_ACCESS_TOKEN')

def data_update():
    if not path.isdir("data"):
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


def extract_data_github():
    with open("data/github.json", "r", encoding="utf-8") as f:
        github_data = json.load(f)
        # print(get(resp[5]).json()[0]["name"])
        return [github_data.get(item) for item in ["login", "avatar_url", "followers", "following", "public_repos",
                                                   "repos_url"]]

def extract_data_codewars():
    with open("data/codewars.json", "r", encoding="utf-8") as f:
        codewars_data = json.load(f)
        return [codewars_data.get(item) for item in ["username", "honor", "leaderboardPosition", "ranks"]]


if __name__ == "__main__":
    data_update()
    print(extract_data_github())
    template = Template(open("index.html", "r", encoding="utf-8").read())
    github_data = extract_data_github()
    codewars_data = extract_data_codewars()
    print(extract_data_codewars())
    rendered_page = template.render(
        github_data=github_data,
        repos_data=get(github_data[5], timeout=10).json(),
        codewars_data=codewars_data
    )
    with open("rendered_index.html", "w", encoding="utf-8") as f:
        f.write(rendered_page)



