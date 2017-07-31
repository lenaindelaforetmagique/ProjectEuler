--[[
PE037.lua
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right
to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right
to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

--]]

function isPrime(a)
  if a==1 then return false end
  local i=2
  while i<=a^(0.5) do
    if a%i==0 then return false end
    i=i+1
  end
  return true
end


function isTruncatablePrime(a)
  if isPrime(a) then
    local N=string.len(tostring(a))
    local i=1
    while isPrime(a%(10^i)) and isPrime(math.floor(a/(10^i))) and i<N do
      i=i+1
    end
    if i==N then return true end
-- right truncatable : a%10
-- left truncatable : math.floor(a/10)
  end
  return false
end

cpt=0
somme=0
i=11
while cpt~=11 do
  if isTruncatablePrime(i) then
    cpt=cpt+1
    somme=somme+i
    print(i)
  end
  i=i+1
end
print("-->",somme)
