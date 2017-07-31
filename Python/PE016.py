##Problem 16
##
##215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
##What is the sum of the digits of the number 21000?


a = 2**1000


s = 0
while a > 0:
    s += a % 10
    a //= 10

print(s)
