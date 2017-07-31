--[[
pe019.lua
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
--]]

DAYS={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
MONTHS={31,28,31,30,31,30,31,31,30,31,30,31}

DATE_INIT={1,1,1,1900}
-- {jour, jour, mois, année}


function nextDay(a)
	a[1]=a[1]%7+1
	a[2]=a[2]%MONTHS[a[3]]+1
	if a[2]==1 then
		a[3]=a[3]%12+1
		if a[3]==1 then
			a[4]=a[4]+1
			if a[4]%100==0 then
				if a[4]%4==0 then MONTHS[2]=29 end
			elseif a[4]%4==0 then
				MONTHS[2]=29
			else
				MONTHS[2]=28
			end
		end
	end
	return a
end

function compDate(a,d,m,y)
	return a[2]==d and a[3]==m and a[4]==y
end

function calDate(d,m,y)
	local a=DATE_INIT
	while not compDate(a,d,m,y) do
		a=nextDay(a)
	end
	return a
end

j=calDate(1,1,1901)
while not compDate(j,31,12,2000) do
	if j[1]==7 and j[2]==1 then compteur=(compteur or 0)+1 end
	j=nextDay(j)
end


print(compteur)




