import logging
import os
from typing import Any
import pandas as pd


logger = logging.getLogger(__name__)


def excel_reader(filename: str, datetime_str: str) -> Any:
    """Получаем аргумент виде xslx файла и дату и возвращаем содержимое"""
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8"):
            data = pd.read_excel(file_path)
            # Переводим второй аргумент в формат datetime
            end_date = pd.to_datetime(datetime_str, format="%d.%m.%Y %H:%M")
            start_date = end_date.replace(day=1)
            # Переводим формат Дата операции в нужный формат
            data["Дата операции"] = pd.to_datetime(
                data["Дата операции"], format="%d.%m.%Y %H:%M:%S"
            )
            # фильтр операций за текущий месяц
            current_month_operations = data[
                (data["Дата операции"] >= start_date)
                & (data["Дата операции"] <= end_date)
            ]
            sum_by_card = (
                current_month_operations.groupby("Номер карты")["Сумма операции"]
                .sum()
                .reset_index()
            )
            cashback = (
                current_month_operations.groupby("Номер карты")["Кэшбэк"]
                .sum()
                .reset_index()
            )
            cashback["Кэшбэк"] = cashback["Кэшбэк"] * 100
            top_5 = current_month_operations.sort_values(
                by="Сумма платежа", ascending=False
            ).head(5)
            logger.info("Удалось открыть xls ура.")
            return (f"Операции за текущий месяц {datetime_str}:\n{current_month_operations}"
                    f"\nСумма операции каждой 'Номер карты':\n{sum_by_card}"
                    f"\n Топ-5 транзакций за месяц{top_5} \nКэшбэк {cashback}")
    except FileNotFoundError:
        return []
