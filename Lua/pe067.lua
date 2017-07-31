--[[
PE067.lua
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
see "pe67_triangle.txt" file

--]]
--

-- lecture du fichier et stockage dans fichier{}
io.input("pe067_triangle.txt",r)
line=nil
fichier={}
i=1
for line in io.lines() do
  fichier[i]=line
  --print(fichier[i])
  i=i+1
end

io.close()

lgFich=table.maxn(fichier)

for i=1,lgFich do
  fichier[i]=string.gsub(fichier[i]," ","")
  local a={}
  local k=1
  for j=1,lgFich do
    a[j]=tonumber(string.sub(fichier[i],k,k+1))
    k=k+2
  end
  fichier[i]=a
end


for i=lgFich-1,1,-1 do
  for j=1,i,1 do
    fichier[i][j]=fichier[i][j]+math.max(fichier[i+1][j],fichier[i+1][j+1])
  end
end

print(fichier[1][1])


















