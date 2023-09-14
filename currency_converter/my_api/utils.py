import requests
import dotenv
import os

#dotenv.load_dotenv(os.path.join('.env'))
#API_KEY = os.getenv('API_KEY')

def get_currency(from_currency, to_currency):
    from_to = from_currency + '' + to_currency
    url = f'https://currate.ru/api/?get=rates&pairs={from_to}&key=1a7d6fd30b7d4b9abfb6d73a7a8f606a'
    response = requests.get(url=url)
    data = response.json().get('data')
    result = data[from_to]
    
    return result


# print(get_currency('USD', 'RUB'))
# print(API_KEY)
