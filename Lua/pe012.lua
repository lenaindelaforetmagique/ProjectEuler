--[[
PE012.lua
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
]]



function old_nbDiv(a)
  local n=1
  for i=1,a/2,1 do
    if a%i==0 then n=n+1 end
  end
  return n
end

function nbDiv(a)
  local n=1
  nb=0
  nMax=a/n
  while n<nMax do
    if a%n==0 then
      nMax=a/n
      if nMax==n then   
        nb=nb+1
      else
        nb=nb+2
      end
    end 
    n=n+1
  end
  return nb
  
end



---[[
--run on the triangle numbers
i=1
k=1
val=nbDiv(k)
while val<500 do
  i=i+1
  k=i*(i+1)/2
  val=nbDiv(k)
  print(k,val)
end
--]]

--print(k,val)








