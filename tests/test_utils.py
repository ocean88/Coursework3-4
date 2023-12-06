from typing import Any
from src.utils import excel_reader


def test_excel_reader() -> Any:
    test_file = 'operations.xls'
    data = excel_reader(test_file, '10.02.2021 16:11')
    assert len(data) > 10
