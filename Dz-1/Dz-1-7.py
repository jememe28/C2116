a = float(input("Первое число: "))
b = float(input("Второе число: "))
do = input("/, *, +, - 1")

if do == "/":
    if a == 0:
        print("На ноль делить нельзя!")
    else:
        print(f"Резултат {a/b}")

if do == "*":
    print(f"Резултат {a*b}")

if do == "+":
    print(f"Резултат {a+b}")
    
if do == "-":
    print(f"Резултат {a-b}")
