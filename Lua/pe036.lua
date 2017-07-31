--[[
PE036.lua
The decimal number, 585 = (1001001001)_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
--]]

function isPalindrom(s)
  -- check if a string is palindromic
  lg=string.len(s)
  local i,j=1,lg
  while i<=j do
    if string.sub(s,i,i)~=string.sub(s,j,j) then
      return false
    end
    i=i+1
    j=j-1
  end
  return true
end

function toBaseN(a,n)
  local s=""
  while a~=0 do
    s=a%n .. s
    a=math.floor(a/n)
  end
  return s
end

somme=0
for i=1,1e6 do
  if isPalindrom(i) and isPalindrom(toBaseN(i,2)) then
    print(i,toBaseN(i,2))
    somme=i+somme
  end
end

print("-->",somme)




