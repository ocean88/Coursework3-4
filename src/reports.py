import logging


def setup_logging() -> logging.Logger:
    """Функция работы логгера возвращает в заданном формате отчет, также example log перезаписывается при запуске"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    file_handler = logging.FileHandler("example.log", mode="w", encoding="UTF-8")
    file_handler.setLevel(logging.INFO)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    logging.getLogger().addHandler(file_handler)
    return logging.getLogger()






