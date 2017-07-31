--[[
PE027.lua
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² - 79n + 1601 was discovered, which produces 80 primes for the
consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n = 0.
--]]



function isPrime(a)
  if a<0 then return false end
  local i=2
  while i<=math.sqrt(a) do
    if a%i==0 then return false end
    i=i+1
  end
  return true
end
--

function lgSeq(a,b)
  local n=0
  while isPrime(n*n+(a*n)+b) do
    --print(n,n^2+(a*n)+b)
    n=n+1
  end
  --print(n,a,b,a*b)
  return n
end


---[[
maxa=nil
maxb=nil
max=0


for a=-999,999 do
  for b=-999,999 do
    local lg=lgSeq(a,b)
    if lg>max then
      max=lg
      maxa=a
      maxb=b
    end
  end
end
--]]

print(max,maxa,maxb,maxa*maxb)





