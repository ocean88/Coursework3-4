from src.utils import excel_reader


def search_data(data, search_query):
    results = []
    for item in data:
        for key, value in item.items():
            if search_query.lower() in str(value).lower():
                results.append(item)
                break
    return results

search_query = input("Enter search query: ")

results = search_data(excel_reader('operations.xls', ''), search_query)

if results:
    for result in results:
        print(result)
else:
    print("No results found.")


