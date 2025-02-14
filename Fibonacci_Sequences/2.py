"""In this instace we want something more dynamic and user-friendly,
   which means that instead of starting with 0 0 1 we will start with two numbers instead
"""


def print_instructions():
    print("Welcome to the Fibonacci game")
    print("Pick two numbers")

print_instructions()

first_num = int(input("Pick the first number: "))
second_num = int(input("Pick the second number: "))
fibonacci_length = int(input("Pick the length of the sequence: "))

# Validate the numbers
while first_num >= second_num:
    print("Remember that the second number must be higher than the first.")
    first_num = int(input("Pick the first number: "))
    second_num = int(input("Pick the second number: "))

third_num = first_num + second_num 

def create_sequence_start():
    sequence = []
    sequence.append(first_num)
    sequence.append(second_num)
    sequence.append(third_num)
    return sequence

def create_fibonacci(sequence):
    while len(sequence) < fibonacci_length:
        sequence.append(sequence[-1] + sequence[-2])  
    return sequence

print_it = create_fibonacci(create_sequence_start())   
print(print_it)
