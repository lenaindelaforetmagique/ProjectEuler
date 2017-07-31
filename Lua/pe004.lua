--[[
PE004.lua
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
]]


--[[ Fonction inventée, équivalente à '#'
function nbCar(n)
  i=1
  while n/10>=1 do
    n=(n-n%10)/10
    i=i+1
  end
  return i
end
--]]

---[[
function isPalindromic(n)
  -- par reccursivité (on part du centre vers l'extérieur pour éviter les zéros)
  --lg=nbCar(n)
  lg=#tostring(n)
  if lg==1 then return true end
  a=math.floor(lg/2)+1  -- position du chiffre lu à gauche
  b=math.ceil(lg/2)     -- position du chiffre lu à droite
  c,d=math.floor(n/(10^(a-1))%10),math.floor(n/(10^(b-1))%10) -- valeurs des chiffres lus
  n=math.floor(n/(10^a))*10^(b-1)+n%(10^(b-1)) -- nouvelle valeur pour n (sans cd)
  --print(a,b,c,d,n)

  --print(a,b,c,d,n)
  return c==d and isPalindromic(n)
  
  
end
--]]



---[[
valMax=0
for i=100,999,1 do
  for j=i,999,1 do
    if isPalindromic(i*j) then
      valMax=math.max(valMax,i*j)
      print(i,j,i*j)
    end
  end

end
print(valMax)
--]]

