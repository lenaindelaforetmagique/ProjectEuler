--[[
PE035.lua
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
--]]

function isPrime(a)
  local i=2
  while i<=a^(0.5) do
    if a%i==0 then return false end
    i=i+1
  end
  return true
end


function isCircularPrime(a)
  local N=string.len(tostring(a))
  local i=1
  while isPrime(a) and i<=N do
    -- permutation circulaire
    local b=math.floor(a/(10^(N-1)))
    a=(a-b*10^(N-1))*10+b
    i=i+1
  end
  if i==N+1 then
    return true
  else
    return false
  end
end

tab={}
cpt=0
for i=2,1e6 do
  if isCircularPrime(i) then
    print(i)
    cpt=cpt+1
    tab[cpt]=i
  end
end
print("-->",cpt)


