--[[
PE007.lua
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
]]

function isPrime(a)
  local i=2
  while i<=a^(0.5) do
    if a%i==0 then return false end
    i=i+1
  end
  return true
end





k=0
i=1
repeat
  i=i+1
  if isPrime(i) then
    k=k+1
    print(k,i)
  end
until k==10001

print(i) --> 104743