def smallest_missing_element(arr):
    
    if arr[0] != 0:
        return 0

    for i in range(len(arr)-1):
        # check the element adjeacent to the current
        # make sure that the adjacent element == current +1
        if arr[i+1] != arr[i] +1:
            # if adj element != current +1 then we know that current +1 should be there
            # but it isn't so return current +1
            return arr[i] + 1
        
    #if we get ouf of the loop and don't find any missing elements
    # return last element plus 1 as the smallest missing value
    return arr[-1] +1


