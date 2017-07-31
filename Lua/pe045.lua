--[[
PE045.lua
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
--]]


function T(n)
  return n*(n+1)/2
end

function isT(n)
  return n==T(math.floor((-1+math.sqrt(1+8*n))/2))
end

function P(n)
  return n*(3*n-1)/2
end

function isP(n)
  return n==P(math.floor((1+math.sqrt(1+24*n))/6))
end

function H(n)
  return n*(2*n-1)
end

function isH(n)
  return n==H(math.floor((1+math.sqrt(1+8*n))/4))
end


i=285+1
while isP(T(i))==false or isH(T(i))==false do
  i=i+1
end

print("-->",T(i))
