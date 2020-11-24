def rearrange_digits(input_list):
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
        
        Args:
        input_list(list): Input List
        Returns:
        (int),(int): Two maximum sums
        """
    
    # sort the numbers using mergesort or quicksort
    # take the first two highest numbers as the start for each value,
    # the second two highest numbers as the second item in the value and so on
    
    sorted_input_list = quicksort(input_list)
    if len(sorted_input_list) < 2:
        print("Cannot build two numbers, list length too small")
        return -1
    
    value1 = "";
    value2 = "";
    for idx, value in enumerate(sorted_input_list):
        if idx % 2 == 0:    # recursively change if even or odd
            value1 += str(value)
        else:
            value2 += str(value)

    return [int(value1), int(value2)]


def sort_a_bit(input_list, start_idx, end_idx):
    
    pivot_idx = end_idx
    pivot_val = input_list[pivot_idx]
    
    while pivot_idx != start_idx:
        
        item = input_list[start_idx]
        
        if pivot_val < item:
            start_idx += 1
            continue
        else:
            input_list[start_idx] = input_list[pivot_idx-1]
            input_list[pivot_idx-1] = pivot_val
            input_list[pivot_idx] = item
            pivot_idx -= 1

    return pivot_idx


def sort_all(input_list, start_idx, end_idx):
    if end_idx <= start_idx:
        return
    pivot_idx = sort_a_bit(input_list, start_idx, end_idx)
    sort_all(input_list, start_idx, pivot_idx-1)
    sort_all(input_list, pivot_idx+1, end_idx)

def quicksort(input_list):
    sort_all(input_list, 0, len(input_list)-1)
    return input_list



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


# own cases
print(rearrange_digits([9,1,2])) # [91, 2]
print(rearrange_digits([0])) # Cannot build two numbers, list length too small
# -1
print(rearrange_digits([0,0,0,0])) # [0, 0], not [00,00]
