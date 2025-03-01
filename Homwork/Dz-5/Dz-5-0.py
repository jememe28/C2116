import requests

def get_usd_to_uah_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    try:
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()

        for currency in data:
            if currency['cc'] == 'USD':
                usd_rate = currency['rate']
                return usd_rate

        return None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

usd_rate = get_usd_to_uah_rate()

if usd_rate:
    print(f"Курс доллара США (USD) к гривне (UAH): {usd_rate} UAH")
else:
    print("Не удалось получить курс USD.")

UAH = float(input("Количество нривен: "))
print(f"{UAH} гривен в доларах США: {round(UAH/usd_rate, 2)}$")