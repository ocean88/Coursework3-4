import logging
import os
from datetime import datetime
import requests
from dotenv import load_dotenv


logger = logging.getLogger(__name__)
load_dotenv()
API_KEY = os.environ.get('API_KEY')
token = os.environ.get('TOKEN')


def get_greeting():
    """Приветствие которое свиряется по текущему часу времени"""
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_exchange_rate():
    """Получаем курсы валют"""
    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    symbols = "RUB"
    headers = {"apikey": API_KEY}
    params_usd = {"symbols": symbols, "base": "USD"}
    params_eur = {"symbols": symbols, "base": "EUR"}

    response_usd = requests.get(base_url, headers=headers, params=params_usd)
    response_eur = requests.get(base_url, headers=headers, params=params_eur)

    data_usd = response_usd.json()
    data_eur = response_eur.json()

    result_usd = data_usd["rates"]
    result_eur = data_eur["rates"]
    logger.info(f"Запрос курса валют")
    return f"Курс доллара {result_usd}\nКурс Евро {result_eur}"


def get_stock_price(symbol: str, token: str) -> str:
    """Получаем курсы акций"""
    api_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            result = data["c"]
            logger.info(f"Успешный запрос finhub")
            return f"Стоимость акций {symbol} - {result}"
        else:
            return f"Запрос не удался код ошибки {response.status_code}"
    except Exception as e:
        return f"Ошибка: {e}"

