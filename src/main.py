from src.logger import setup_logging
from src.views import get_greeting, get_exchange_rate, get_stock_price
from src.utils import excel_reader
from src.services import search_in_data
from src.reports import filter_by_category


logger = setup_logging()


print(get_greeting())
print(excel_reader("operations.xls", "10.02.2021 16:11"))
print(get_exchange_rate())
token = "clmrde1r01qjj8i8tolgclmrde1r01qjj8i8tom0"
print(get_stock_price("AAPL", token))
print(get_stock_price("AMZN", token))
print(get_stock_price("GOOGL", token))
print(get_stock_price("MSFT", token))
print(get_stock_price("TSLA", token))
"""1 раздел Веб страницы выводится результат за месяц,
 может поменять месяц с помощью 2го аргумента+курсы валют"""

print(search_in_data("operations.xls", "Сбербанк"))
"""2 раздел выводим по поиску все что содержит слово Сбербанк,
 из описаний или категорий"""

print(filter_by_category("operations.xls", "Связь", "16.09.2020"))
"""3 раздел выводит через аргумент последние три 3 месяца,
декоратор записывает в файл mylog.txt"""
