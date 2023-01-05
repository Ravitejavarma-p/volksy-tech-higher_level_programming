#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        x = my_list[0]
        if len(my_list) < 1:
            return None
        if i > x:
            x = i
    return i        
