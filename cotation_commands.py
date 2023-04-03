import requests
import json

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

async def get_dollar_cotation():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return float(data["USDBRL"]["bid"])
        else:
            raise Exception('Erro ao acessar a API')
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado. {e}")


async def get_euro_cotation():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return float(data["EURBRL"]["bid"])
        else:
            raise Exception('Erro ao acessar a API')
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado. {e}")
