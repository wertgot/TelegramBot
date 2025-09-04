import requests
import json
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/getMe'

response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    data = response.json()
    pretty_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_json)
else:
    print(response.status_code)  # При другом коде ответа выводим этот код