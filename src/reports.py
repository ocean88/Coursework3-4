import os
import pandas as pd
from typing import Optional, Callable, Any
import logging
from functools import wraps
import datetime, timedelta


logger = logging.getLogger(__name__)


def report(*, filename: str = "report.xlsx") -> Callable:
    """Записывает в файл результат, который возвращает функция, формирующая отчет"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Optional[Any], **kwargs: Optional[Any]) -> Optional[Any]:
            try:
                result = func(*args, **kwargs)
                if filename.endswith(".xlsx"):
                    result.to_excel(filename, index=False)
                else:
                    raise ValueError("Файл некорректного формата")
            except Exception:
                logger.info("Что то пошло не так")
                result = None
            return result

        return inner

    return wrapper


@report()
def filter_by_category(
    filename: str, search_data: str, date: Optional[str] = None
) -> Any:
    """Функций получает xls файл, и слово по которому будет возвращаться результат"""
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        data = pd.read_excel(file_path)
        data["Категория"] = data["Категория"].fillna("")
        data["Дата платежа"] = pd.to_datetime(data["Дата платежа"], dayfirst=True)

        if date is None:
            date = pd.to_datetime(datetime.now(), dayfirst=True)
        else:
            date = pd.to_datetime(date, dayfirst=True)

        three_months_ago = date - pd.DateOffset(months=3)

        filtered_data = data[
            (data["Категория"].str.contains(search_data, case=False))
            & (data["Дата платежа"] >= three_months_ago)
            & (data["Дата платежа"] <= date)
        ]
        logger.info("Успешно отработала функция")
        return filtered_data

    except FileNotFoundError:
        return []
