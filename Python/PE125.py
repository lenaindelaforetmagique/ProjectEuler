##Problem 125
##
##The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2.
##
##There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
##
##Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.


def isPalindrome(a):
    s=str(a)
    return s[::-1] == s


vmax = 10**8

s = set()

t = [i**2 for i in range(1, int(vmax**0.5)+1)]
for i in range(len(t)-1):
    j = i+1
    r = t[i]+t[j]
    while r < vmax and j < len(t):
        if isPalindrome(r):
            print(r, t[i], t[j])
            s.add(r)
        j += 1
        r += t[j]

print(">>", sum(s))
        
        
        
        
