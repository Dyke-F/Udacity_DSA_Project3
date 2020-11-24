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

sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
