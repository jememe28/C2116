import requests
from bs4 import BeautifulSoup

url = 'https://sinoptik.ua/ru/pogoda/sloviansk'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    date = soup.find('p', class_='date').get_text(strip=True)
    print(f"Дата: {date}")
    
    weather_table = soup.find('div', class_='weatherDetails')
    
    for row in weather_table.find_all('tr'):
        time = row.find('td', class_='time')
        temp = row.find('td', class_='temperature')
        
        if time and temp:
            print(f"Время: {time.get_text(strip=True)}, Температура: {temp.get_text(strip=True)}")
else:
    print("Ошибка: Не удалось получить данные с сайта.")