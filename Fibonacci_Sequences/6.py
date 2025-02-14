"""this time we will use a single function to create 
the starting numbers""" 

def create_list():
    list_ = [] 
    def add_to_the_list():
        for a in range(3):
            a += 1
            list_.append(a)  
    add_to_the_list()  
    return list_
#we attacj tje fimctopm tp a varoab;e wjocj a;sp stpres ot sp we cam ise ot as a parameter later on



"""and a single function to generate the remaining fibonacci
the list_f will take a function as an argument so it can use its return as the foundation for the fibonacci
On the other hand, the length parameter will decide how long the fibonacci sequence will be 
"""

def create_fibonacci(list_f, length):
    a = 0
    while a < length:
          a += 1
          next_item = list_f[-1] + list_f[-2]
          list_f.append(next_item)
    print(list_f)
      
"""as the list grows the last and second last items change by default, which achieves dynamism"""

create_fibonacci(create_list(), 20)    
