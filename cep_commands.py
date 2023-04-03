import requests
import json

url = 'https://cep.awesomeapi.com.br/json/'

async def get_cep(cep):
    try:
        response = requests.get(url + cep)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        elif response.status_code == 400:
            raise Exception('cep Inválido')
        elif response.status_code == 404:
            raise Exception('cep não encontrado')
    except Exception as e:
        raise Exception(e)