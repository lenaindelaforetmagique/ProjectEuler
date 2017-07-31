--[[
PE050.lua
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

--]]

dofile("DIVlib.lua")
-- include nextPrime(n)
-- include isPrime(n)


-- écriture de la table des nbres premiers

NBMAX=1e6

n=nextPrime(0)
i=0
prime={}
while n<NBMAX do
  --print(n)
  i=i+1
  prime[i]=n
  n=nextPrime(n)

end
print("-->nb premiers",i,table.maxn(prime))

lgTab=table.maxn(prime)

-- lecture de la table.
--boucle sur la lgChaine
  --boucle sur le début de chaine
    --vérif de la somme
    --vérif de prime
--

somme=0
trouve=false
lgChaine=0

repeat
	lgChaine=lgChaine+1
	somme=somme+prime[lgChaine]
until somme>=NBMAX



--lgChaine=lgTab -- diminue jusqu'à trouver la première chaine valide
while (not trouve) and lgChaine>1 do
	print("lgChaine",lgChaine)
  somme=0
  local posDeb=1

  while (not trouve) and posDeb<=lgTab-lgChaine+1 do
	--print("posDeb",posDeb)
    if posDeb==1 then
      for i=1,lgChaine do
        somme=somme+prime[i]
      end
    else
      somme=somme-prime[posDeb-1]+prime[posDeb+lgChaine-1]
    end
    if somme<NBMAX then
      if isPrime(somme) then
        trouve=true
      end
	else
      --print("break")
	  break
    end
    posDeb=posDeb+1 -- on se déplace vers la droite de la table
  end

  if not trouve then
    lgChaine=lgChaine-1 -- on diminue la taille de la chaine
  end
end


print("-->",somme,lgChaine)



























