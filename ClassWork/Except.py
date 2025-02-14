try:
    num = int(input("num 1:"))
    num2 = int(input("num 2:"))
    print(num / num2)

except ZeroDivisionError:
    print("Деление на ноль невозможно")
except ValueError:
    print("Введені числа не є числом")

