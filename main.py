from requests import get
from os import environ
import json


CODEWARS_USER_NAME = environ.get('CODEWARS_USER_NAME')

cw_resp = get("https://www.codewars.com/api/v1/users/{}".format(CODEWARS_USER_NAME))
with open('data/codewars.json', 'w') as f:
    json.dump(cw_resp.json(), f, indent=4)
