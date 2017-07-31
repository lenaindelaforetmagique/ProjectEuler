--[[
PE040.lua
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
--]]


function d(k)
  local n=1
  while k>n*(10^n-10^(n-1)) do
    k=k-(n*(10^n-10^(n-1)))
    n=n+1
  end
  local nombre=10^(n-1)-1+math.ceil(k/n)
  k=k%n
  if k~=0 then k=n-k end
  k=k+1
  return math.floor(nombre/(10^(k-1)))%10
end


prod=1
for i=0,6,1 do
  --print(d(i))
  prod=prod*d(10^i)
end
print("-->",prod)


--[[

s=""
i=1
while string.len(s)<1e6 do
  s=s..i
  --print(i)
  i=i+1
end

prod=1
for i=0,6 do
  prod=string.sub(s,10^i,10^i)*prod
end
print("-->",prod)
--]]

