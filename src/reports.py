import os
import pandas as pd
from typing import Optional, Callable, Any
import logging
from functools import wraps
import datetime


logger = logging.getLogger(__name__)


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{now} {func.__name__} ok\n")
                        file.write(f"{result}\n")
                else:
                    print(f"{now} {func.__name__} ok")
                    print(f"Result: {result}")
                return result
            except Exception as e:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                inputs = f"Inputs: {args}, {kwargs}"
                error_message = f"{func.__name__}: {str(e)}"
                log_message = (
                    f"{now} {func.__name__} error: " f"{error_message}. {inputs}\n"
                )
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                raise e

        return inner

    return wrapper


@log(filename="mylog.txt")
def filter_by_category(
    filename: str, search_data: str, date: Optional[str] = None
) -> Any:
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)

        data = pd.read_excel(file_path)

        data["Категория"] = data["Категория"].fillna("")
        data["Дата платежа"] = pd.to_datetime(data["Дата платежа"], dayfirst=True)

        if date is None:
            date = pd.to_datetime(datetime.datetime.now(), dayfirst=True)
        else:
            date = pd.to_datetime(date, dayfirst=True)

        three_months_ago = date - pd.DateOffset(months=3)

        filtered_data = data[
            (data["Категория"].str.contains(search_data, case=False))
            & (data["Дата платежа"] >= three_months_ago)
            & (data["Дата платежа"] <= date)
        ]

        json_data = filtered_data.to_json(orient="records", force_ascii=False)

        return json_data

    except FileNotFoundError:
        return []
