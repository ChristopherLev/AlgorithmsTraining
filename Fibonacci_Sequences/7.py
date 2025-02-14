# Reversed Fibonacci 
main_list = [2, 5, 7]


for a in range(10):
    next_item = main_list[1] - main_list[0]
    main_list.insert(0, next_item)
    
print(main_list)
