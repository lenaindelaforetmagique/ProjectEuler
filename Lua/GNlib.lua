--[[
-- GNlib.lua
 Bibliothèque de fonctions pour le calcul des grands nombres entiers
 sans limite de taille et sans perte.
 Le principe est le découpage des grands nombres par paquet de GN_DIM digits.
 Les opérations suivent cette logique.
--]]


GN_DIM=7 -- nb digits

--
function StringtoGN(s)
  local a={}
  local i=1
  while string.len(s)>0 do
    a[i]=tonumber(string.sub(s,math.max(1,string.len(s)-GN_DIM+1),string.len(s)))
    s=string.sub(s,1,math.max(0,string.len(s)-GN_DIM))
    i=i+1
  end
  return a
end

--
function GNtoString(a)
  local s=""
  local flag="%0".. GN_DIM .. "i"
  for i=1,table.maxn(a)-1,1 do
      s=string.format(flag,a[i] or 0) .. s
  end
  s=a[table.maxn(a)] .. s
  return s
end

--
function GN_add(a,b) -- a+b; a,b GN
  local sum={}
  local carry=0
  local size=math.max(table.maxn(a),table.maxn(b))
  local i=1
  while (i<=size or carry~=0) do
    local t1=(a[i] or 0)
    local t2=(b[i] or 0)
    sum[i]=(t1+t2+carry)%(10^GN_DIM)
    carry=((t1+t2+carry)-(t1+t2+carry)%(10^GN_DIM))/(10^GN_DIM)
    i=i+1
  end
  return sum
end

--
function GN_mult(a,b) -- a*b; a,b GN
  local s_a=table.maxn(a)
  local s_b=table.maxn(b)
  local prod={}
  for i=1,s_a do
    local carry=0
    local j=1
    while (j<=s_b or carry~=0) do
      local t1=(prod[i+j-1] or 0)+(a[i] or 0)*(b[j] or 0)+carry
      prod[i+j-1]=t1%(10^GN_DIM)
      carry=(t1-t1%(10^GN_DIM))/(10^GN_DIM)
      j=j+1
    end 
  end
  return prod
end

--

function GN_pow(a,b) -- a^b; a GN, b normal integer
  local result=StringtoGN("1")
  for i=1,b do
    result=GN_mult(result,a)
  end
  return result
end
--

function print_GN(a)
  print(GNtoString(a))
end
--

function GN_sumDigit(a)
  local sum=0
  for i=1,table.maxn(a) do
    for j=1,GN_DIM do
      sum=sum+math.floor(a[i]/(10^(j-1)))%10
    end
  end
  return sum
end
--



function GN_cmpr(a,b)-- returns -1,0,1 (A>B,A==B,A<B)
  local n=math.max(table.maxn(a),table.maxn(b))
  local i=n
  while (a[i] or 0)==(b[i] or 0) and i>0 do
    i=i-1
  end
  if i==0 then
    return 0
  elseif (a[i] or 0)>(b[i] or 0) then
    return 1
  else
    return -1
  end
end
--






















