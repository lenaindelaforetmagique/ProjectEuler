--[[
PE046.lua
It was proposed by Christian Goldbach that every odd composite number can be written as the
sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a
square?
--]]

dofile("DIVlib.lua")
-- include isPrime(n)



i=9
while true do
  if not isPrime(i) then
    j=1
    while (not isPrime(i-2*j^2)) and i-2*j^2>1 do
      j=j+1
    end
    if i-2*j^2<=1 then
      break
    else
      print(i,"=",i-2*j^2,"+2*",j,"^2")
    end
  end
  i=i+2
end

print("-->",i)


