sequence = [0, 1, 1] #starting sequence
sequence_2 = [0, 1, 1, 2]
count = 0 #starting count for the while statement 

def create_fib(sequence):
    #get last two items 
    itemone = sequence[len(sequence) - 1] #get the last 
    itemtwo = sequence[len(sequence) - 2] #and the second last item
    next_item = itemone + itemtwo #the next item is their sum
    sequence.append(next_item) #the next item gets added to the sequence
    
    """Due to the dynamic values of itemone + itemtwo 
    every time an item gets added we instantly get a new last 
    and second last item 
    
    """
#setting the limit for the sequence 
while count < 15: #setting the limit to 15 numbers after the first 3
    create_fib(sequence) #item gets added based on the function's specs
    create_fib(sequence_2)
    count += 1 #count increases 
    
print(sequence)    
print(sequence_2)
