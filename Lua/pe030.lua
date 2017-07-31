--[[
PE030.lua

Surprisingly there are only three numbers that can be written as the sum of fourth powers of
their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

---------
NOTE PERSONNELLE :
On peut montrer que, si :
 - digits = 2, le maxi en puissance_n est 2*9^n, le nombre mini est 10,
 - digits = 3, maxPowN=3*9^n(), nbMini=100
 - digits = 4, maxPowN=4*9^n, nbMini=1000
 - digits = 5, maxPowN=5*9^n, nbMini=10000
 - digits = 6, maxPowN=6*9^n(354294), nbMini=100000 --> OK
 - digits = 7, maxPowN=7*9^n(413343), nbMini=1000000 --> Impossible
 
DONC le nombre max de recherche est 354294


--]]



N=6

function isNpower(a,n)
  local b=a
  local lg=string.len(tostring(a))
  local verif=0
  for i=1,lg do
    local c=b%10
    verif=verif+c^n
    b=(b-c)/10
  end
  return a==verif
end

i=1
while(i*9^N>=10^(i-1)) do i=i+1 end
imax=(i-1)*9^N
print(imax)





somme=0
for i=2,imax do
  if isNpower(i,5) then
    print(i)
    somme=somme+i
  end
end

print(somme)









