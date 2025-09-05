import requests
import time
import json
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

API_URL = 'https://api.telegram.org/bot'
TEXT = 'KYS'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={-1}').json()

    '''pretty_json = json.dumps(updates, indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_json)'''

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1