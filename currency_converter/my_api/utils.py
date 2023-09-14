import requests
import dotenv
import os

dotenv.load_dotenv(os.path.join('.env'))
API_KEY = os.getenv('API_KEY')

def get_currency(from_currency, to_currency):
    from_to = from_currency + '' + to_currency
    url = f'https://currate.ru/api/?get=rates&pairs={from_to}&key={API_KEY}'
    response = requests.get(url=url)
    data = response.json().get('data')
    return data[from_to]
