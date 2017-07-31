--[[
PE038.lua
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576
the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n  1?
--]]


dofile("DIVlib.lua")
-- includes fact(n)

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



function isConcatenated(a)
  -- boucle sur nb de digits du premier terme
  local s_a=tostring(a)
  local i=1
  local test=false
  local nb
  repeat
    nb=string.sub(s_a,1,i)
    local s_e=nb
    local j=2
    while string.len(s_e)<string.len(s_a) do
      s_e=s_e.. j*nb
      j=j+1
    end
    i=i+1
    test=(s_e==s_a)
    --print(i,s_e,test)
  until test or i>4
  return test
end




i=0

repeat
  nbre=permut(9,1,i)
  test=isConcatenated(nbre)
  --print(i,nbre,test)
  i=i+1
until test

print("-->",nbre)







