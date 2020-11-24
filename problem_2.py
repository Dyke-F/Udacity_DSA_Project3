def _pivot_detection(input_list):
    
    lowest_left = 0 # if sorted, would be the lowest value in the list
    # if values on the right to it are larger, continue exploring
    start = 0
    end = len(input_list) -1
    
    while start <= end:
        center = (start+end) // 2
        if input_list[center] > input_list[lowest_left]: # check more on the right
            start = center+1
        if input_list[center] < input_list[lowest_left]: # check more on the left
            end = center
        if input_list[center] < input_list[center-1]:    # if we reach a node thats smaller than its left
            # node we reached the pivot !
            break

    return center, input_list[center]



def rotated_array_search(input_list, number):
    """
        Find the index by searching in a rotated sorted array
        
        Args:
        input_list(array), number(int): Input array to search and the target
        Returns:
        int: Index or -1
        """
    if len(input_list) == 1:
        return 0
    
    pivot_idx, pivot = _pivot_detection(input_list)

    # recursive function to check in sublists, split by pivot_idx
    def _rec_bs(search_list, number, start, end):
        if start > end:
            return -1
        center_idx = (start+end) // 2
        center = search_list[center_idx]
        if center == number:
            return center_idx
        elif center > number:
            return _rec_bs(search_list, number, start, center_idx-1)
        elif center < number:
            return _rec_bs(search_list, number, center_idx+1, end)
    
    # number must be in the right half
    if number < input_list[0]:
        search_list = input_list[pivot_idx:]
        search_list_center_idx = _rec_bs(search_list, number, 0, len(search_list)-1)
        return search_list_center_idx + len(input_list[:pivot_idx]) # add indices from left half

    # number in left half
    else:
        search_list = input_list[:pivot_idx]
        search_list_center_idx = _rec_bs(search_list, number, 0, len(search_list)-1)
        return search_list_center_idx


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Own tests

# edge case 1
print(rotated_array_search([1], 1)) # 0

# edge case 2
print(rotated_array_search([1,2,3,4,0], 5)) # -1

# normal case 3
print(rotated_array_search([1,2,3,4,0], 0)) # 4
