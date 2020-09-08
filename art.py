#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

#day of the week as an integer, where Monday is 0 and Sunday is 6.
dayn = datetime.datetime.today().weekday()
if (dayn < 6):
	dayn = dayn +1
	nexd = dayn +1
else: 
	dayn = 0
	nexd = 1

f    = open("pacman", "r")
line = f.readlines()
curr = line[dayn]
#f.close()
poz = 0 #deff value
if   "v" in curr:
	print("ok")
	poz = curr.find("v")	
	print "poz:", poz
	#git commit
elif "n" in curr:
	print("no")
	poz = curr.find("n")

#get nextday char:
next_day_char = line[nexd][poz]

if  (next_day_char == '.'):
#	nl = line[nexd].replace('.','n',poz+1)
	nextact = "n"
elif(next_day_char == 'x'):
	nextact = "v"

#	
newline_list  	  = list(line[nexd])
newline_list[poz] = nextact
newstr 		  = "".join(newline_list)
#
oldline_list	  = list(line[curr])
oldline_list[poz] = oldchar
oldstr		  = "".join(oldline_list)

print "today ", curr
print "nextd ", newstr

#change current

#print "dayn", dayn, line[dayn]
#print "next", nexd, line[nexd], ndc
