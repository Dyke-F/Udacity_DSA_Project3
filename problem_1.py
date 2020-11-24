def sqrt(number = None):
    """
        Calculate the floored square root of a number
        
        Args:
        number(int): Number to find the floored squared root
        Returns:
        int: Floored Square Root
        """
    
    # base cases
    if number == None:
        print("Give a valid input")
    elif number < 0:
        raise ValueError("*** Square root of negative input number is not defined ***")
    elif number == 0:
        return number
    elif number == 1:
        return number
    
    # calculate square root
    else:
        return binary_search_SQRT(number, start=0, end=number//2)


def binary_search_SQRT(number, start, end):
    """ Applies a binary search to find the square root of a number. """
    
    # end = number // 2; end is always higher than the sqrt value,
    # but lower than the number itself, so decreases number of iterations
    
    while start <= end:
        center = (start + end) // 2     # middle value
        
        # base case
        if center ** 2 == number:
            return center
        
        # if the middle value squared is lower than our number, set the
        # lower middle threshold to center +1
        elif center ** 2 < number:
            start = center +1
            
            # if no integer sqrt of our number exists:
            # check as follows: lower integer **2 is lower than our number,
            # next integer (center+1) squared is already higher than the number
            # ---> true square root lies in between center and center +1
            # check how to round the value: if the difference between our number and
            # center**2 is lower than (center+1)**2 return center, if (center+1)**2
            # is closer to the true number return center+1
            
            if (center**2 < number) and (center+1)**2 > number:
                diff_low = number - (center**2)
                diff_up  = ((center+1)**2) - number
                if diff_low < diff_up:
                    return center
                else:
                    return center+1
        
        # if center**2 is higher than our number, decrease the upper boundary
        # of the binary search algorithm
        
        else:
            end = center -1



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# Own test cases

# edge case 1: empty input
print(sqrt()) # give a valid input

# edge case 2: high number
print(sqrt(100000)) # 316
assert 317**2 > sqrt(100000)**2 > 315**2, "Calculation is wrong"

# normal case
print(sqrt(100)) # 10
