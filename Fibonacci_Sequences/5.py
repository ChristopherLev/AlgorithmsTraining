limit_ = 20
fibonacci = []
a = 0

def grab_input(*args):
    if args[-1] < args[-2]:
        args[-1], args[-2] = args[-2], args[-1]
        #we append them as the lower number first, and the higher second
    fibonacci.append(args[-2])
    fibonacci.append(args[-1])    
grab_input(10, 45, 65, 8000, 9000)

#we now expand the fibonacci 
while a < 20:
     a += 1
     fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)   