class Human():
    age = 20
    name = "Nick"

class Student(Human):
    study = True

class Worker(Student):
    study = False
    work = True
    profesion = "engeniar"

nick = Human()
ann = Student()
don = Worker()

print(nick.age, nick.name)
print(ann.age, ann.name, ann.study)
print(don.age, don.name, don.study, don.profesion)