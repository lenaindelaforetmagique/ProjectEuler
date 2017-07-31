--[[
PE060.lua

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce
another prime.

--]]

dofile("DIVlib.lua")
-- includes isPrime(a)
-- includes nextPrime(a)
-- includes nPrime(n,t)


NB=5

prime={}

print(nPrime(1120,prime))

function blah(n,prime,s_i,e_i,t)
  --print(n)
  for i=s_i,e_i do
    if testReussi(t,n,prime[i]) then
      --print("--",n)
      t[n]=prime[i]
      if n<NB then
        --print(table.concat(t,"-"))
        blah(n+1,prime,i+1,e_i,t)
      else
        local somme=0
        for j=1,table.maxn(t) do
          somme=somme+t[j]
        end
        print(table.concat(t,"+"),"=",somme)
        
      end
    end
  end
end
--

function testReussi(t,n,c)
  local test=true
  for i=1,n-1 do
    test=test and isPrime(concat(t[i],c)) and isPrime(concat(c,t[i])) 
  end
  --print(n,test)
  return test
  
end
--


function concat(a,b)
  local len = math.floor(math.log10(b))+1
  return a*10^len+b
end
--

t={}
print(blah(1,prime,1,1120,t))

















