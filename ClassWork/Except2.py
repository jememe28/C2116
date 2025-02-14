words = ["hi", "hello", "cherry"]

try: 
    index = int(input("Index: "))
    word = words[index]
    print(f"Word with index {index}: {word}")

except IndexError:
    print("This index dosen't exist")
except ValueError:
    print("Index is not int value")