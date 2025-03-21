import requests

GEMINI_API_URL = 'https://api.gemini.com/v1/pubticker/btcusd'  # Exemplo de URL da API
GEMINI_API_KEY = 'AIzaSyCmFWODWWmR-TYceGn0x2CRKDJ4miK5d9E'

def get_gemini_data():
    headers = {
        'X-GEMINI-APIKEY': GEMINI_API_KEY,
    }
    response = requests.get(GEMINI_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None