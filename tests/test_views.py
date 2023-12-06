import datetime
from src.views import get_greeting


def test_get_greeting():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        expected_result = "Доброй ночи"
    elif 12 <= current_hour < 18:
        expected_result = "Добрый день"
    elif 18 <= current_hour < 22:
        expected_result = "Добрый вечер"
    else:
        expected_result = "Доброй ночи"
    actual_result = get_greeting()
    assert actual_result == expected_result, (f"Expected: {expected_result}"
                                              f"but got: {actual_result}")
