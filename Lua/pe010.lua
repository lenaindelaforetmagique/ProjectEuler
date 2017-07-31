--[[
PE010.lua
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below one million.
]]

function isPrime(a)
  local i=2
  while i<=a^(0.5) do
    if a%i==0 then return false end
    i=i+1
  end
  return true
end


somme=0
i=2
while i<2e6 do
  print(i)
  if isPrime(i) then somme=somme+i end
i=i+1
end

print(somme)

