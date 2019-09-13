import sys

'''This solution uses the concept of memoization to avoid
duplicate work
'''

def female(n, memo):
    """ Create unique key for each value of N and store result in the hashmap
    passed as an argument ("memo"). Check at the beginning of the function if this key
    already exists in the map. If so, we already computed this so return the
    value immediately.
    """
    key = "F" + str(n)
    if key in memo:
        return memo[key]
    if n == 0:
        return 1
    ret_val = n -  male(female(n - 1, memo), memo)
    memo[key] = ret_val
    return ret_val


def male(n, memo):
    key = "M" + str(n)
    if key in memo:
        return memo[key]
    if n == 0:
        return 0
    ret_val = n - female(male(n-1, memo), memo)
    memo[key] = ret_val
    return ret_val


if __name__ == "__main__":
    n = sys.argv[1]
    flist = []
    mlist = []
    memo = dict()

    for i in range(0,int(n)):
        flist.append(female(i, memo))
        mlist.append(male(i, memo))
    print("F: {}".format(flist))
    print("M: {}".format(mlist))
