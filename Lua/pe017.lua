--[[
pe017.lua
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
--]]

units={
  "one","two","three","four","five","six","seven","eight","nine","ten",
  "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"
  }
decades={"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"}
hundred="hundred"
thousand={"thousand","million","billion","quadrillion","quintillion","sextillion"}

W_and="and"
W_hyphen="-"
W_space=" "

--1234
function toWords(nbre)
  i=0
  s=""
  a=nbre
  while a>0 do
    if a%1000>0 then
      s=toWords_1_999(a%1000) .. W_space .. (thousand[i] or "") .. W_space .. s
    end
    a=(a-a%1000)/1000
    i=i+1
  end
  
  return s
  
end
--
function toWords_1_999(nbre)
  local s=""
  local d=nbre%100
  local h=(nbre-d)/100

  -- d compris dans [1;99]
  if d>0 then
    if d<20 then
      s=units[d] .. s
    else
      if d%10>0 then
        s=W_hyphen .. units[d%10] .. s
      end
      s=decades[(d-d%10)/10-1] .. s
    end
  end
  
  if h>0 then
    if d>0 then s=W_and .. W_space .. s end
    s=units[h] .. W_space .. hundred .. W_space .. s
  end
  return s
end
--


somme=0
for i=1,1000,1 do
 somme=somme+string.len(toWords(i))
end
print(somme)










