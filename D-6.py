b = int(input("Ваша оценка: "))

if b in range(0, 49):
    print("незадовільно")

elif b in range(50, 69):
    print("задовільно")

elif b in range(70, 89):
    print("добре")

elif b in range(90, 100):
    print("відмінно")