--[[
PE005.lua
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
]]


function ppcm(a,b)
  a,b=math.max(a,b),math.min(a,b)
  n=a
  while not (n%b==0 and n%a==0) do
    n=n+1
  end
  return n
end

n=1
for i=1,20,1 do
  n=ppcm(i,n)
  print(n)
end
print(n)

function fact(n)
  if n==0 then return 1 end
  return n*fact(n-1)
end
