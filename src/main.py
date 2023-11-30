from src.reports import setup_logging
from src.views import get_greeting
from src.utils import excel_reader


logger = setup_logging()

print(get_greeting())
print(excel_reader('operations.xls', '10.02.2021 16:11'))



