class Human():
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
ann = Worker()

print(nick.height)
print(ann.height)