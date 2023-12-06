from typing import Any
from src.services import search_in_data


def test_search_in_data() -> Any:
    test_file = 'operations.xls'
    data = search_in_data(test_file, 'Сбербанк')
    assert len(data) > 10
