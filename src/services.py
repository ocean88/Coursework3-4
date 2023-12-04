import logging
import os
from typing import Any
import pandas as pd

logger = logging.getLogger(__name__)


def search_in_data(filename: str, search_data: str) -> Any:
    """Получаем аргумент в виде xslx файла и возвращаем содержимое"""
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8"):
            data = pd.read_excel(file_path)
            filtered_data = data[
                (data["Описание"].str.contains(search_data, case=False))
                | (data["Категория"].str.contains(search_data, case=False))
            ]

            json_data = filtered_data.to_json(orient="records",
                                              force_ascii=False)

            return json_data
    except FileNotFoundError:
        return []
