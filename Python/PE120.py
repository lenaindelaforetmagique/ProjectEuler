##Problem 120
##
##Let r be the remainder when (a−1)**n + (a+1)**n is divided by a**2.
##
##For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49.
##And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
##
##For 3 ≤ a ≤ 1000, find ∑ rmax.
"""
(a-1)**n + (a+1)**n = 2*sum(a**(n-i)*C_n_i) pour i dans[0,n], pair
"""

som = 0
for a in range(3, 1001):
    if a%2 == 0:
        som += a*(a-2)
    else:
        som += a*(a-1)

print(som)



