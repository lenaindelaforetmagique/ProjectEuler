--[[
PE023.lua
A perfect number is a number for which the sum of its proper divisors is exactly equal to
the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is
called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
--]]

NBMAX=28123

function SumDiv(a)
  local r=0
  for i=1,a-1,1 do
    if a%i==0 then
      r=r+i
    end
  end
  return r
end


tab={}

for i=1,NBMAX do
  tab[i]=(SumDiv(i)>i)
  --print(i,tab[i])
end

--[[
test sur tous les nombres
--]]

somme=0

for i=1,NBMAX do
  local j=1
  local k=i-j
  while (k>0) and not(tab[j] and tab[k]) do
    j=j+1
    k=i-j
  end
  if k<=0 then
    somme=somme+i
    --print(i,k)
  end

end
somme2=0
for i=1,NBMAX do
somme2=somme2+i
end


print(somme,somme2)








