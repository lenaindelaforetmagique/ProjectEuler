--[[
PE034.lua
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
--]]

--[[
Pour un nombre à n digits, la somme des factorielles de ses chiffres est au maximum n*9!
Le plus petit nombre à n digits est 10^(n-1)
n*9<10^(n-1) survient quand n=8
>nmax=7
>Nmaxi=10^7-1
--]]


function fact(a)
  if a==0 then
    return 1
  else
    return a*fact(a-1)
  end
end



function sumFact(a)
  local somme=0
  while a~=0 do
    local b=a%10
    a=(a-b)/10
    somme=somme+fact(b)
  end
  return somme
end

somme=0
for i=10,1e7-1 do
  --print(i)
  if i==sumFact(i) then
    somme=somme+i
    print(i)
  end
end


print(somme)



