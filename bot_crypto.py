from requests import Session
import telegram
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

def save_data_BTC(data_coin):
    with open('data.txt', 'w') as outfile:
        json.dump(data_coin, outfile)

def read_data_BTC():
    with open('data.txt', 'r') as file:
        data_crypto = json.load(file)
    out = {}
    for d in data_crypto['data']:
        if d['id'] in [1027,1]:
            #print(d)
            out[d['name']]=d
    return out

def coin(api_key_CMC):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key_CMC,
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return data


def read_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    creator = config['creator']
    id_bot = config['id_bot']
    chat_id = config['chat_id']
    api_key_CMC = config['api_key_CMC']
    return id_bot, chat_id, api_key_CMC

def send_message(data, id_bot, chat_id):
    myBot = telegram.Bot(token=id_bot)
    #print(myBot)
    coins_all = ['Bitcoin','Ethereum']
    now = datetime.now()
    now = now.strftime("%d / %B / %Y -- %H:%M:%S")
    line = '---------------------------------'
    a = str(now) + '\n' + line
    for coin in coins_all:
        a = a + '\n' + \
        'Nombre = ' + data[coin]['name']+'\n'+ \
        'Simbolo = ' + data[coin]['symbol']+'\n'+ \
        'Ranking = ' + str(data[coin]['cmc_rank'])+'\n'+ \
        'Ultima actualizacion = ' + str(data[coin]['last_updated'])+'\n'+ \
        'Precio = ' + str(data[coin]['quote']['USD']['price'])+'\n'+ \
        'Cambio en la ultima hora = ' + str(data[coin]['quote']['USD']['percent_change_1h'])+'% \n'+ \
        'Cambio en las ultimas 24 horas = ' + str(data[coin]['quote']['USD']['percent_change_24h'])+'% \n'+ \
        'Cambio en los ultimos 7 dias = ' + str(data[coin]['quote']['USD']['percent_change_7d'])+'% \n'+ \
        'Cambio en los ultimos 30 dias = ' + str(data[coin]['quote']['USD']['percent_change_30d'])+'% \n'+ \
        'Markep Cap = ' + str(data[coin]['quote']['USD']['market_cap'])+'\n'+line
    myBot.send_message(chat_id=chat_id, text=a)

def main():
    id_bot, chat_id,api_key_CMC = read_config()
    #data_coin = coin(api_key_CMC)
    #save_data_BTC(data_coin)
    data = read_data_BTC()
    send_message(data,id_bot,chat_id)
    

if __name__ == '__main__':
    main()
