##Problem 112
##
##Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
##
##Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
##
##We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
##
##Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
##
##Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
##
##Find the least number for which the proportion of bouncy numbers is exactly 99%.

def bouncy(n):
    s = str(n)
    t = [c for c in s]
    t.sort()
    if ''.join(t) == s:
        return 1
    elif ''.join(t[::-1]) == s:
        return -1
    else:
        return 0


cible = 99/100
s = 0
N = 99

while s/N < cible:
    if bouncy(N+1) == 0:
        s += 1
    N += 1

print(N)

