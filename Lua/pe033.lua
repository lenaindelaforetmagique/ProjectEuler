--[[
PE033.lua
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of
the denominator.
--]]


num={}
denom={}
i=1
for a=1,9 do
  for b=1,9 do
    for c=1,9 do
      local nbA=10*a+b
      local nbB=10*b+c
      if nbA*c==nbB*a and nbA~=nbB then
        num[i]=math.min(nbA,nbB)
        denom[i]=math.max(nbA,nbB)
        i=i+1
      end
    end
  end
end
--

function pgcd(a,b)
  if a<b then a,b=b,a end
  if b==0 then return a end
  return pgcd(b,a%b)
end
--

prodNum=1
prodDenom=1
for i=1,table.maxn(num) do
  print(num[i],"/",denom[i])
  prodNum,prodDenom=prodNum*num[i],prodDenom*denom[i]
end

print(prodDenom/pgcd(prodDenom,prodNum))
