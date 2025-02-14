"""A fibonacci requires at least two starting nums
and by default the second num must be bigger than the first 
"""
def create_start(*args): #we use the * operator for multiple positional arguments
    if len(args) > 2:
        return create_start(*args[:2])  # Pass only the first two arguments
    if args[0] > args[1]:
        return create_start(args[1], args[0])  # Swap the values and rerun
    return args
    
#creation of the first three numbers of the fibonacci
fibonacci_ = list(create_start(3, 1))
third_num = int(fibonacci_[-1] + fibonacci_[-2])
fibonacci_.append(third_num)

#generation of the actual fibonacci_
for a in range(12):
    next_num = fibonacci_[-1] + fibonacci_[-2]
    fibonacci_.append(next_num)
    
print(fibonacci_)    