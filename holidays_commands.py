import os
import requests
import json
from urllib.parse import urlencode


url = 'https://calendarific.com/api/v2/holidays'
api_key = os.getenv("CALENDARIFIC_API_KEY")

async def get_holidays(year):
    try:
        params = {'api_key': api_key, 'country': 'BR', 'year': year}
        query_string = (urlencode(params))
        full_url = f"{url}?{query_string}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado. {e}")
