'''
Input: an integer
Returns: an integer
'''
# with cache, every n value is only computed once
# cache reduces runtime from O(n^3) to O(n) becuase now n is only computed once
# we did increase space complexity to do this
def eating_cookies(n, cache):

    if n < 0:
        return 0
    if n == 0:
        return 1
    # check the cash to see if it holds the answer this branch needs
    elif n in cache:
        return cache[n]
    else:
        # otherwise n is not in the cache, so we need to compute answer via recursive calls
        # once the answer is computed, save it in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 101

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")

