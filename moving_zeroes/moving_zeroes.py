'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # search array for 0s
    # Iterate list inversely to avoid skipping lists elements if existing loop’s list 
    # is changed if list were to iterated normally. 
    # This can be done using [::-1] to iterate the list from the back to front.
    for i in range(len(arr))[::-1]:
        # if zero, pop and append a new zero
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1] 
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")