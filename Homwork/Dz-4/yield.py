class IterableWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        def generator():
            current = self.start
            while current < self.end:
                yield current
                current += 1
        return generator()

iterable = IterableWithGenerator(1, 5)

for value in iterable:
    print(value)