import sys

'''Naive mutually recursive solution, this is extremely slow. Will
optimize using memoization'''
def female(n):
    if n == 0:
        return 1
    return  n -  male(female(n - 1))

def male(n):
    if n == 0:
        return 0
    return n - female(male(n-1))

if __name__ == "__main__":
    n = sys.argv[1]
    flist = []
    mlist = []

    for i in range(0,int(n)):
        flist.append(female(i))
        mlist.append(male(i))
    print("F: {}".format(flist))
    print("M: {}".format(mlist))
