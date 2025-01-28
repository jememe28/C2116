import random
a = random.randrange(1, 10)
b = 3
print("Компьютер заглдал число")
print(a)
def game():
    global b, a
    while b != 0:
        d = int(input("Вы думаете что это число: "))
        if d < a:
            b -= 1
            print("Больше")

        elif d > a:
            b -= 1
            print("Меньше")

        elif d == a:
            print("Вы победили!")
            quit()

    print("Вы проиграли...")
game()
        
