##Problem 188
##
##The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:
##
##a↑↑1 = a,
##a↑↑(k+1) = a(a↑↑k).
##
##Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.
##
##Find the last 8 digits of 1777↑↑1855.



def puiss(a, b):
    r = 1
    for i in range(b):
        r = (r * a)%10**8

    return r


def tetration(a, k):
    if k == 1:
        return a
    else:
        return puiss(a, tetration(a, k-1)%10**8)%10**8

print(tetration(1777,3))
