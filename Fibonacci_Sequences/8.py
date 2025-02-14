n = 10
main_list = [0, 1, 1]
"""a quick reminder that comprehensions can also be used as stand alone literals 
#if we assigned this to a variable it would also return 'None None None" while the for a in range(n' loop was going on 
"""
[main_list.append(main_list[len(main_list)-1] + main_list[len(main_list)-2]) 
                    for a in range(n)]
print(main_list)                    

#now the main_list gets appended with what was generated inside the comprehension