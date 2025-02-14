#in this example we will use classes and objects to generate a fibonacci


class Fibonacci:
    def __init__(self, first, second):
        self.sequence = [first, second]
#the sequence which we will expand is consisted by the first two numbers
#that are picked by the user

    def generate(self, n): #n represents the argument passed to the method
        while len(self.sequence) < n: 
            next_item = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_item)
        return self.sequence

# we create an instance of the fibonacci class 
fib = Fibonacci(0, 1)

# we generate fibonacci numbers according to it 
print(fib.generate(10))
