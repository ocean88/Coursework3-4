from typing import Any
from src.reports import filter_by_category


def test_filter_by_category() -> Any:
    test_file = 'operations.xls'
    data = filter_by_category(test_file, '10.02.2021 16:11')
    assert len(data) == 2
