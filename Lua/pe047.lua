--[[
PE047.lua
The first two consecutive numbers to have two distinct prime factors are:

14 = 2*7
15 = 3*5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2²*7*23
645 = 3*5*43
646 = 2*17*19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
--]]


function nbPrimeFactors(n)
  local a=2
  local cpt=0
  while n~=1 do
    if n%a==0 then
      --print(a)
      cpt=cpt+1
      repeat
        n=n/a
      until n%a~=0
    end
    a=a+1
  end
  return cpt
end
--

NOMBRE=4

i=2
compteur=0
while compteur<NOMBRE do
  if nbPrimeFactors(i)==NOMBRE then
    --print(i)
    compteur=compteur+1
  else
    compteur=0
  end
  i=i+1

end
i=i-NOMBRE

print("-->",i)









