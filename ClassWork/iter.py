class Counter:
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num
    
    def __iter__(self):
        self.i - 0
        return self
    
    def __next__(self):
        self.i += 1
        if self.i >self.max_num:
            raise StopIteration
        return self.i

count = Counter(5)

for i in count:
    print(i)



