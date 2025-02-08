class Hello_world(): 
    hello = "Hello" 
    _hello = "_Hello" 
    __hello = "__Hello"
 
    def __init__(self): 
        self.world = "World" 
        self._world = "_World" 
        self.__world = "__World"
 
    def printer(self): 
        print(self.hello) 
        print(self._hello) 
        print(self.__hello) 
        print(self.world) 
        print(self._world) 
        print(self.__world)
        
class Hi(Hello_world):
    def hi_print(self): 
        print(self.hello) 
        print(self.world) 
        print(self._hello) 
        print(self._world) 
        print(self.__hello)
        print(self.__world)
 
hello = Hello_world() 
hello.printer()

hi = Hi() 
hi.hi_print()