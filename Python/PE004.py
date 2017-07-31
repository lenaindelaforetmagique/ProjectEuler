##Problem 4
##
##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##
##Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(a):
    s=str(a)
    return s[::-1] == s

#l = []
vMax=1
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i * j) and i*j>vMax:
            #l.append(i * j)
            vMax = i * j

#l.sort(key = lambda x:-x)
print(vMax)
        
