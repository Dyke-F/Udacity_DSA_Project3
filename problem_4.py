def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """
    
    
    D = {}
    new_list = []
    for value in input_list:
        D.setdefault(value, []).append(value)
    sorted_D = sorted(D.items(), key=lambda x: x[0])
    for key, vals in sorted_D:
        for val in vals:
            new_list.append(val)
    
    return new_list

def sort_012(input_list):
    
    i = 0
    nxt0 = 0
    nxt2 = len(input_list) -1
    
    while i <= nxt2:
        if input_list[i] == 0:
            input_list[i] = input_list[nxt0]
            input_list[nxt0] = 0
            i +=1
            nxt0 += 1
        elif input_list[i] == 2:
            input_list[i] = input_list[nxt2]
            input_list[nxt2] = 2
            nxt2 -= 1
        else:
            i +=1
    
    return input_list
    

    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# own tests
# edge case 1
print(sort_012([0])) # [0]
# edge case 2
print(sort_012([0,0])) # [0, 0]
# case 3
print(sort_012([0,1,2])) # [0, 1, 2], already sorted
