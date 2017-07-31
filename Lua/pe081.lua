--[[
PE081.lua

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by only moving to the right and down, is indicated in bold red and is
equal to 2427.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331


Find the minimal path sum, in matrix.txt (right click and
'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from
the top left to the bottom right by only moving right and down.

--]]

DIM=80


-- lecture du fichier et stockage dans fichier{}
io.input("pe081_matrix.txt",r)
line=nil
fich={}
i=1
for line in io.lines() do
  fich[i]=line
  i=i+1
end
io.close()


for i=1,table.maxn(fich) do
  local lgLine=string.len(fich[i])
  local t={}
  local c_s=1
  local c_e=string.find(fich[i],',') --,c_s)
  local j=1
  while c_e>c_s do
    t[j]=tonumber(string.sub(fich[i],c_s,c_e-1))
    c_s=c_e+1
    c_e=string.find(fich[i],',',c_s) or lgLine+1
    j=j+1
  end
  fich[i]=t
end

--fich=nil
--fich={{131,673,234,103,18},{201,96,342,965,150},{630,803,746,422,111},{537,699,497,121,956},{805,732,524,37,331}}

res={}
for i=1,DIM do
  local t={}
  res[i]=t
end

for i=1,DIM do -- ligne
  for j=1,DIM do -- colonne
    --print(i,j,fich[i][j])
	if i==1 then
	  res[i][j]=(res[i][j-1] or 0)+fich[i][j]
	elseif j==1 then
	  res[i][j]=(res[i-1][j] or 0)+fich[i][j]
	else
      res[i][j]=math.min(res[i][j-1],res[i-1][j])+fich[i][j]
	end
  end
end
print("-->",res[DIM][DIM])

