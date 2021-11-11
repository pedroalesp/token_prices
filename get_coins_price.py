#Este programa hace un request a la api de Coin Market Cap y trae datos del top 10 de tokens

import requests

headers = {
    'X-CMC_PRO_API_KEY': 'e3238e46-ef8e-4dcd-a053-492ea0450877',
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'



#Esta decoración recibe a la función get_data la cual se encarga de hacer el request a la API de CoinMarketCap
#Se recibe la data desordenada y en la nested function se ordena y se filtra por los datos que queremos, nombre, token y precio actual
def get_coin_prices_dec(func):
    def wrapper():
        for dict in func():
            print(dict['name'], '-', dict['symbol'], '-', 'Price:',round(dict['quote']['USD']['price'], 2), 'USD') 

    return wrapper

def run():
    @get_coin_prices_dec
    def get_data():
        json = requests.get(url, params=params, headers=headers).json()
        data = json['data']
        #print(data)
        return data
    
    get_data()


if __name__ == '__main__':
    run()