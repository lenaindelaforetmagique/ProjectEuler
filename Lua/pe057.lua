--[[
PE057.lua
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
--]]

--[[
if an iteration gives a/b ratio, the next ratio is (2*b+a)/(a+b)
because f(x):=1+1/(1+f(x-1))
initialisation with a,b=1,1
--]]

dofile("GNlib.lua")

compteur=0
a,b=StringtoGN("1"),StringtoGN("1")
GN_2=StringtoGN("2")
for i=1,1000 do
  local c=GN_add(GN_mult(b,GN_2),a)
  local d=GN_add(a,b)
  if string.len(GNtoString(c))>string.len(GNtoString(d)) then
    compteur=compteur+1
  end
  a,b=c,d
end

print("-->",compteur)

