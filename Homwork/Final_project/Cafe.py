import random

class Cafe:
    def __init__(self):
        self.fame = 50  # Известность кафе (0-100)
        self.balance = 200  # Баланс кафе
        self.coffee_price = 5  # Цена за чашку кофе
        self.cost_per_coffee = 2  # Затраты на производство одной чашки кофе
        self.visitors_today = 0  # Количество посетителей за день
        self.total_visitors = 0  # Общее количество посетителей
        self.days_passed = 0  # Количество прошедших дней
        self.fame_per_visitor = 1  # Известность, которую приносит один посетитель
        self.advertising_cost = 100  # Стоимость рекламы
        self.upgrade_cost = 200  # Стоимость улучшения кафе
        self.current_event = None  # Текущий ивент

    def set_coffee_price(self, price):
        """Установить цену на кофе."""
        if price < self.cost_per_coffee:
            print("Цена не может быть ниже себестоимости!")
        else:
            self.coffee_price = price
            print(f"Цена на кофе установлена: ${price}")

    def buy_advertising(self):
        """Купить рекламу для увеличения известности."""
        if self.balance >= self.advertising_cost:
            self.balance -= self.advertising_cost
            self.fame += 10  # Реклама увеличивает известность
            self.fame = min(100, self.fame)  # Ограничение известности до 100
            print("Реклама куплена! Известность кафе увеличилась.")
        else:
            print("Недостаточно средств для покупки рекламы.")

    def upgrade_cafe(self):
        """Улучшить кафе, чтобы посетители приносили больше известности."""
        if self.balance >= self.upgrade_cost:
            self.balance -= self.upgrade_cost
            self.fame_per_visitor += 0.5  # Улучшение увеличивает известность от посетителей
            print("Кафе улучшено! Посетители теперь приносят больше известности.")
        else:
            print("Недостаточно средств для улучшения кафе.")

    def generate_event(self):
        """Генерация случайного события."""
        events = [
            {"description": "Кафе было оштрафовано за несоблюдение санитарных норм.", "effect": "balance", "value": -200},
            {"description": "Кафе получило положительный отзыв в газете!", "effect": "fame", "value": 10},
            {"description": "В кафе произошла небольшая кража.", "effect": "balance", "value": -100},
            {"description": "Кафе посетил известный блогер!", "effect": "fame", "value": 15},
            {"description": "Соседнее кафе закрылось, и клиенты перешли к вам.", "effect": "fame", "value": 5},
            {"description": "Цены на кофе выросли из-за проблем с поставками.", "effect": "cost_per_coffee", "value": 1},
            {"description": "Кафе выиграло конкурс 'Лучшее кафе города'!", "effect": "fame", "value": 20},
            {"description": "Сломался кофейный аппарат, пришлось потратиться на ремонт.", "effect": "balance", "value": -150},
        ]
        self.current_event = random.choice(events)

    def apply_event(self):
        """Применить эффект текущего ивента."""
        if self.current_event:
            event = self.current_event
            if event["effect"] == "balance":
                self.balance += event["value"]
            elif event["effect"] == "fame":
                self.fame += event["value"]
                self.fame = max(0, min(100, self.fame))  # Ограничение известности
            elif event["effect"] == "cost_per_coffee":
                self.cost_per_coffee += event["value"]
            print(f"Ивент: {event['description']}")
            self.current_event = None  # Сбрасываем ивент после применения

    def simulate_day(self):
        """Симуляция одного дня работы кафе."""
        # Генерация ивента
        self.generate_event()

        # Количество посетителей зависит от известности и цены на кофе
        self.visitors_today = random.randint(0, self.fame) - int(self.coffee_price * 2)
        self.visitors_today = max(0, self.visitors_today)  # Не может быть меньше 0

        # Расчет доходов и расходов
        revenue = self.visitors_today * self.coffee_price
        costs = self.visitors_today * self.cost_per_coffee
        profit = revenue - costs

        # Обновление баланса
        self.balance += profit

        # Обновление общего количества посетителей и дней
        self.total_visitors += self.visitors_today
        self.days_passed += 1

        # Известность увеличивается в зависимости от посетителей и улучшений
        self.fame += int(self.visitors_today * self.fame_per_visitor)
        self.fame = max(0, min(100, self.fame))  # Ограничение известности от 0 до 100

        # Вывод результатов дня
        print("\n--- Результаты дня ---")
        print(f"Посетителей сегодня: {self.visitors_today}")
        print(f"Доход: ${revenue}")
        print(f"Расходы: ${costs}")
        print(f"Прибыль: ${profit}")
        print(f"Баланс: ${self.balance}")
        print(f"Известность кафе: {self.fame}%")

        # Применение ивента
        self.apply_event()

    def show_status(self):
        """Показать текущее состояние кафе."""
        print("\n--- Текущее состояние кафе ---")
        print(f"Баланс: ${self.balance}")
        print(f"Цена на кофе: ${self.coffee_price}")
        print(f"Известность: {self.fame}%")
        if self.current_event:
            print(f"Ивент: {self.current_event['description']}")

    def show_info(self):
        """Показать дополнительную информацию."""
        while True:
            average_visitors = self.total_visitors / self.days_passed if self.days_passed > 0 else 0
            print("\n--- Информация о кафе ---")
            print(f"1. Затраты на производство кофе: ${self.cost_per_coffee} за чашку")
            print(f"2. Среднее количество посетителей за день: {average_visitors:.2f}")
            print(f"3. Общее количество посетителей: {self.total_visitors}")
            print(f"4. Количество прошедших дней: {self.days_passed}")
            print(f"5. Текущая известность: {self.fame}%")
            print(f"6. Текущий баланс: ${self.balance}")
            print(f"7. Текущая цена на кофе: ${self.coffee_price}")
            print(f"8. Известность от одного посетителя: {self.fame_per_visitor:.1f}")
            print(f"9. Стоимость рекламы: ${self.advertising_cost}")
            print(f"10. Стоимость улучшения кафе: ${self.upgrade_cost}")
            print("11. Вернуться в основное меню")

            choice = input("Ваш выбор: ")

            if choice == "11":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

def main():
    cafe = Cafe()
    days = 1

    print("Добро пожаловать в игру 'Управление кафе'!")
    print("Ваша задача — управлять кафе, устанавливать цены, улучшать его и следить за прибылью.")

    while True:
        print(f"\n--- День {days} ---")
        cafe.show_status()
        print("\nЧто вы хотите сделать?")
        print("1. Установить цену на кофе")
        print("2. Продолжить день")
        print("3. Показать информацию о кафе")
        print("4. Купить рекламу")
        print("5. Улучшить кафе")
        print("6. Выйти из игры")

        choice = input("Ваш выбор: ")

        if choice == "1":
            try:
                price = float(input("Введите новую цену на кофе: $"))
                cafe.set_coffee_price(price)
            except ValueError:
                print("Пожалуйста, введите число!")
        elif choice == "2":
            cafe.simulate_day()
            days += 1
            if cafe.balance < 0:
                print("\nВаше кафе обанкротилось! Игра окончена.")
                break
            # Ожидание подтверждения для продолжения
            input("\nНажмите 1 и Enter, чтобы продолжить...")
        elif choice == "3":
            cafe.show_info()
        elif choice == "4":
            cafe.buy_advertising()
        elif choice == "5":
            cafe.upgrade_cafe()
        elif choice == "6":
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()