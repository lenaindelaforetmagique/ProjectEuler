--[[
PE054.lua
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest,
in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in
each hand are compared (see example 4 below); if the highest cards tie then the next highest
cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner

P1:5H 5C 6S 7S KD
P2:2C 3S 8S 8D TD
->P2

P1:5D 8C 9S JS AC
P2:2C 5C 7D 8S QH
->P1

P1:2D 9C AS AH AC
P2:3D 6D 7D TD QD
->P2

P1:4D 6S 9H QH QC
P2:3D 6D 7H QD QS
->P1

P1:2H 2D 4C 4D 4S
P2:3C 3D 3S 9S 9D
->P1

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
--]]
--

dofile("DIVlib.lua")
-- includes quickSort(t)


---[[ lecture du fichier et stockage dans liste{}
io.input("pe054_poker.txt",r)
line=nil
liste={}
i=1
for line in io.lines() do
  liste[i]=line
  --print(liste[i])
  i=i+1
end

io.close()

for i=1,table.maxn(liste) do
  liste[i]=string.gsub(liste[i]," ","")
  local t={}
  t[1],t[2]=string.sub(liste[i],1,10),string.sub(liste[i],11,20)
  liste[i]=t
  --print(liste[i][1],liste[i][2])
end

--]]

function note_hand(s) -- returns a note from a valid hand
  local _,isFlush=string.gsub(s,string.sub(s,2,2),"_")
  isFlush=isFlush==5

  local values={'2','3','4','5','6','7','8','9','T','J','Q','K','A'}
  for k,v in pairs(values) do
    values[v]=k
  end
  local t={}
  for i=1,5 do
    t[i]=values[string.sub(s,i*2-1,i*2-1)]
  end
  quickSort(t)
  
  local isStraight=true
  for i=2,5 do
    isStraight=isStraight and t[i]-t[i-1]==1
  end
  
  -- Flush or Straight.
  if isFlush and isStraight then
    return t[5]*14^12 -- straight flush
  elseif isStraight then
    return t[5]*14^8 -- straight
  elseif isFlush then
    local score=0
    for i=1,5 do
      score=score+t[i]*14^(i-1)
    end
    return 14^9+score -- flush
  end
  
  -- 
  local cpt={}
  local max=0
  for i=1,5 do
    cpt[t[i]]=(cpt[t[i]] or 0)+1
    max=math.max(max,cpt[t[i]])
  end
  
  if max==4 then
    local i=0
    repeat
      i=i+1
    until (cpt[i] or 0)==4
    return i*14^11 -- four of a kind
  elseif max==3 then
    local i=0
    repeat
      i=i+1
    until (cpt[i] or 0)==3
    local j=0
    repeat
      j=j+1
    until (cpt[j] or 0)==2 or j>13
    if j>13 then
      return i*14^7 -- three of a kind
    else
      return i*14^10 -- full house
    end
  else --if max==2 then
    local i=0
    local score=0
    repeat
      i=i+1
    until (cpt[i] or 0)==2 or i>13
    if i<=13 then score=score+i*14^5 end-- first pair
    local j=i
    repeat
      j=j+1
    until (cpt[j] or 0)==2 or j>13
    if j<=13 then
      score=score+j*14^6
    end
    local pow=0
    for k=1,5 do
      if t[k]~=i and t[k]~=j then
        score=score+t[k]*14^pow
        pow=pow+1
      end
    end
    return score
  end
  --print(table.concat(t,"-"),isStraight,isFlush)

end
--

cpt=0
---[[
for i=1,table.maxn(liste) do
  --print(i,liste[i][1],liste[i][2],note_hand(liste[i][1])>note_hand(liste[i][2]))
  if note_hand(liste[i][1])>note_hand(liste[i][2]) then
    cpt=cpt+1
  end
end
print("-->",cpt)
--]]





















