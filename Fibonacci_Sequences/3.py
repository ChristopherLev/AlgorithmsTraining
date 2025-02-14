#in this example I wish to avoid repeating the input() function
main_list = []
b = -1

for a in range(2):
    str_list = ["First", "Second"]
    b += 1
    c = str_list[b]
    d = int(input(f"Please enter the {c} number: "))    
    main_list.append(d)

#if the first number is greater than the second, then, they will change places

if main_list[1] < main_list[0]:
    main_list[0], main_list[1] = main_list[1], main_list[0]
    
#we now have the starting nums based on user input 


#we are now ready to generate the actual fibonacci 
for a in range(10):
    main_list.append(main_list[-1] + main_list[-2])
    
print(main_list)        
    
    