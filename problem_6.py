import math

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    min_val = math.inf
    max_val = -math.inf
    
    for i in ints:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
            
    return (min_val, max_val)


# tests

print(get_min_max([0,0])) # (0,0)
print(get_min_max([-10,100, 30, 20, 10])) # (-10, 100)
print(get_min_max([-math.inf, 10, 30, 50, 100])) #(-inf, 100)

