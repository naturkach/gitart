#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

#day of the week as an integer, where Monday is 0 and Sunday is 6.
dayn = datetime.datetime.today().weekday()
print "day:", dayn
if (dayn < 6):
	dayn = dayn +2
#	nexd = dayn +2
else: 
	dayn = 0
#	nexd = 1

#f    = open("pacman", "r")
#line = f.readlines()
#curr = line[dayn]

with open('pacman', 'r') as f1, open('pacman.tmp' , 'w') as f2:
	lines = f1.readlines()
#	curr  = lines[dayn]
	poz = 10 #deff value
	strn= 0
		
	for line in lines:
		strn = strn + 1 
		line = line.strip()
		#print (strn, line)
		#curr = line[dayn]
		#print ('curr', curr)	
		if (dayn == strn):
			print strn, line, "today"
		else:
			print strn, line
'''	
		if   "v" in curr:
			print("ok")
			poz 	= curr.find("v")	
			print "poz:", poz
			oldchar = "x"
		elif "n" in curr:
			print("no")
			poz = curr.find("n")
			oldchar = "."

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

		oldline_list	  = list(line[dayn])
		oldline_list[poz] = oldchar
		oldstr		  = "".join(oldline_list)
#curr[poz] = "z"
		print "today ", curr
		print "nextd ", newstr
		print "old   ", oldstr
		f2.write(oldstr)
'''

#change current

#print "dayn", dayn, line[dayn]
#print "next", nexd, line[nexd], ndc
