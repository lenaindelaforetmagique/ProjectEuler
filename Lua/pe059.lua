--[[
PE059.lua

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each
byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key
is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a
password as a key. If the password is shorter than the message, which is likely, the key is
repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted 
ASCII codes, and the knowledge that the plain text must contain common English words, decrypt
the message and find the sum of the ASCII values in the original text.

--]]


-- 1 charger le fichier
io.input("pe059_cipher1.txt",r)
line=nil
fich=""

for line in io.lines() do
  fich=fich .. line
end

io.close()


fich=string.gsub(fich,"\n","")
--fich=string.gsub(fich,"","")
lgFich=string.len(fich)
t={}
c_s=1
c_e=string.find(fich,',') --,c_s)
i=1
while c_e>c_s do
  t[i]=string.sub(fich,c_s,c_e-1)
  c_s=c_e+1
  c_e=string.find(fich,',',c_s) or lgFich+1
  i=i+1
end

for i=1,table.maxn(t) do
  t[i]=tonumber(t[i])
end




-- 65 a 122



function XORdecrypt(t,key)
  local lgKey=table.maxn(key)
  key[0]=key[lgKey]
  local t2={}
  for i=1,table.maxn(t) do
    t2[i]=bit32.bxor(t[i],key[i%lgKey])
  end
  return t2
end
--



for i=0,26^3-1 do
  local key={}
  local a=i
  key[1]=a%26+97
  a=math.floor(a/26)
  key[2]=a%26+97
  a=math.floor(a/26)
  key[3]=a%26+97
  local res=XORdecrypt(t,key)
  local s=''
  local res2={}
  for j=1,table.maxn(res) do
    res2[j]=string.char(res[j])
  end
  s=table.concat(res2)
  if string.match(s," and ")~=nil then
    print(table.concat(key,"-"))
    print(s)
    somme=0
    for k=1,table.maxn(res) do
      somme=somme+res[k]
    end
    print("-->",somme)
  end
end


















