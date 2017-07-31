--[[
-- DIVlib.lua
 Bibliothèque de fonctions diverses.
 quickSort(table,Position tete de lecture, derniere position)
 pgcd(a,b)
 
 isPrime(a)
 isPandigital(a)
 
 
--]]

function quickSort(t,s_i,e_i)
  s_i=s_i or 1
  e_i=e_i or table.maxn(t)
  
  if s_i>=e_i then return t end
  --print(s_i,e_i)
  
  --local tampon
  local pivot=t[s_i] -- choisi arbitrairement en pos 1
  
  -- calcule la position définitive du pivot
  local posPivot=s_i
  for i=s_i,e_i do
    if pivot>t[i] then posPivot=posPivot+1 end
  end
  -- switch pivot
  t[s_i],t[posPivot]=t[posPivot],t[s_i]
  
  -- ordre
  for i=s_i,posPivot-1 do
    if t[i]>=pivot then
      -- i contient la position d'un elt à envoyer de l'autre côté du pivot
      for j=posPivot+1,e_i do
        if t[j]<pivot then
          -- switch
          t[i],t[j]=t[j],t[i]
        end
      end
    end
  end
  t=quickSort(t,s_i,posPivot-1)
  t=quickSort(t,posPivot+1,e_i)
  
  return t
end
--

function nextPerm(t)
  -- 1 position du pivot
  local i=table.maxn(t)-1
  while t[i]>t[i+1] do i=i-1 end
  local pivot=i
  
  -- 2 incrémenter le pivot > adresse du suivant
  local k
  for i=pivot+1,table.maxn(t) do
    if t[i]>t[pivot] then
      if t[i]<(t[k] or math.huge) then k=i end
    end
  end
  t[pivot],t[k]=t[k],t[pivot]
  k=nil
  -- 3 trier ce qui est à droite du pivot
  t=quickSort(t,pivot+1)
  -- 4 return t

  --return t
end
--

function pgcd(a,b)
  a,b=math.abs(a),math.abs(b)
  if a<b then a,b=b,a end
  if b==0 then return a end
  return pgcd(b,a%b)
end
--

function ppcm(a,b)
  return a*b/pgcd(a,b)
end
--

function fact(a)
  if a<=0 then
    return 1
  else
    return a*fact(a-1)
  end
end
--


local prime_mem={}

function isPrime(a)
  if prime_mem[a]==nil then
    if a<=1 then
      prime_mem[a]=false
      return false
    end
    local i=2
    while i<=a^(0.5) do
      if a%i==0 then
        prime_mem[a]=false
        return false
      end
      i=i+1
    end
    prime_mem[a]=true
    return true
  else
    return prime_mem[a]
  end
end
--

function ppfp(n) --renvoie le plus petit facteur premier
  for i=2,n^(0.5),1 do
    if isPrime(i) then
      if n%i==0 then return i end
    end
  end
  return n
end
--

function pgfp(n) --renvoie le plus grand facteur premier
  for i=math.floor(n^(0.5)),2,-1 do
    if isPrime(i) then
      if n%i==0 then return i end
    end
  end
  return n
end
--

function decompPrime(n,t)
  local a=0
  fact=ppfp(n)
  
  while fact~=n do
    a=a+1
    t[a]=fact
    n=n/fact
    fact=ppfp(n)
  end
    a=a+1
    t[a]=fact
    return t
end
--

function decompPrime2(n,t) --sans répétition du facteur premier
  local a=0
  fact=ppfp(n)
  
  while fact~=n do
    if t[a]~=fact then
      a=a+1
      t[a]=fact
    end
    n=n/fact
    fact=ppfp(n)
  end
    if t[a]~=fact then
      a=a+1
      t[a]=fact
    end
    return t
end
--


function nextPrime(n)
  repeat
    n=n+1
  until isPrime(n)
  return n
end
--

function nPrime(n,t)
  if t[n]==nil then
    local i=table.maxn(t)
    while i<n do
      i=i+1
      t[i]=nextPrime(t[i-1] or 0)
    end
  end
  return t[n]
end
--

function isPandigital(a)
  local s=tostring(a)
  local lg=string.len(s)
  if lg>9 then return false end
  local i=1
  while string.find(s,i)~=nil do
    i=i+1
  end
  if i>lg then
    return true
  else
    return false
  end
end
--

