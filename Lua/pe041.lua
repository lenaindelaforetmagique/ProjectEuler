--[[
-- PE041.lua
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
--]]

--[[
all 9-digit pandigital numbers are divisible by 9 (9+8+7+6+5+4+3+2+1=45>4+5>9)
all 8-digit pandigital numbers are divisible by 9 (8+7+6+5+4+3+2+1=36>3+6>9)
start with 7-digitn numbers
--]]

dofile("DIVlib.lua")

function permut(s_i,e_i,n)
  local nbVal=math.abs(e_i-s_i)+1
  if n<0 or n>fact(nbVal)-1 then return 0 end

  -- initialise la chaine de lecture s_l
  local s_l=""
  for i=s_i,e_i,(e_i-s_i)/math.abs(e_i-s_i) do
    s_l=s_l .. i
  end

  -- écriture du nbre avec les carac disponibles dans s_w
  local s_w=""
  for i=1,nbVal do
    local lec=math.floor(n/fact(nbVal-i))+1
    n=n%fact(nbVal-i)
    s_w=s_w .. string.sub(s_l,lec,lec)
    s_l=string.gsub(s_l,string.sub(s_l,lec,lec),"")
  end
  return tonumber(s_w)
end

-- boucle sur nbDigits
nbDigit=7
test=true
nombre=0
while test do
  -- boucle sur les nombres à nbDigits
  local i=0
  while test and i<fact(nbDigit) do
    nombre=permut(nbDigit,1,i)
	print(i, nombre)
    test=not isPrime(nombre)
    i=i+1
  end
  nbDigit=nbDigit-1
end

print("-->",nombre)
print(isPrime(nombre))





