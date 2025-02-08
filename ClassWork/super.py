class Class1():
    ver = 20
    def __init__(self):
        self.ver = 10
class Class2(Class1):
    def __init__(self):
        print(self.ver)
        super().__init__()
        print(self.ver)
        print(super().ver)

hello_world = Class2()