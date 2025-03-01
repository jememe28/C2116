import requests
from bs4 import BeautifulSoup

# Шаг 1: Указываем URL сайта с погодой
url = 'https://sinoptik.ua/ru/pogoda/sloviansk'

# Шаг 2: Отправляем запрос к сайту и получаем HTML-код страницы
response = requests.get(url)

# Шаг 3: Проверяем, что запрос прошел успешно
if response.status_code == 200:
    # Шаг 4: Парсим HTML-код с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Шаг 5: Ищем дату на странице
    date = soup.find('p', class_='date').get_text(strip=True)
    print(f"Дата: {date}")
    
    # Шаг 6: Ищем блок с почасовой погодой
    weather_table = soup.find('div', class_='weatherDetails')
    
    # Шаг 7: Проходим по каждой строке таблицы
    for row in weather_table.find_all('tr'):
        # Шаг 8: Ищем время и температуру в строке
        time = row.find('td', class_='time')
        temp = row.find('td', class_='temperature')
        
        # Шаг 9: Если время и температура найдены, выводим их
        if time and temp:
            print(f"Время: {time.get_text(strip=True)}, Температура: {temp.get_text(strip=True)}")
else:
    print("Ошибка: Не удалось получить данные с сайта.")