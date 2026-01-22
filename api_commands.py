import os
import requests
from dotenv import load_dotenv

def get_data_from_api(endpoint):
    load_dotenv() # take environment variables from .env
    baseURL = "https://www.thebluealliance.com/api/v3/"
    API_KEY = os.getenv("API_BLUE")
    headers = {
        'X-TBA-Auth-Key': API_KEY
    }
    response = requests.get(baseURL+endpoint, headers=headers)
    #200 is good
    if response.status_code == 200:
        #Returns the json as a list
        return response.json()
    else:
        response.raise_for_status()
