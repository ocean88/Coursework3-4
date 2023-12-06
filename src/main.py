import json
import os
from src.logger import setup_logging
from src.views import get_greeting, get_exchange_rate, get_stock_price
from src.utils import excel_reader
from src.services import search_in_data
from src.reports import filter_by_category


logger = setup_logging()


def get_combined_results():
    """Сохранение результатов в JSON-файл"""
    token = os.environ.get('TOKEN')

    # Результаты функций
    results = {
        "greeting": get_greeting(),
        "widget_data": excel_reader("operations.xls", "10.02.2021 16:11"),
        "exchange_rate": get_exchange_rate(),
        "AAPL_stock_price": get_stock_price("AAPL", token),
        "AMZN_stock_price": get_stock_price("AMZN", token),
        "GOOGL_stock_price": get_stock_price("GOOGL", token),
        "MSFT_stock_price": get_stock_price("MSFT", token),
        "TSLA_stock_price": get_stock_price("TSLA", token),
        "search_results": search_in_data("operations.xls", "Сбербанк"),
        "filtered_results": filter_by_category("operations.xls", "Связь", "16.09.2020").to_json()
    }

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False)

    # Возвращаем результаты в виде JSON-объекта
    return json.dumps(results, ensure_ascii=False)


print(get_combined_results())
