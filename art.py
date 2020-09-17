#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

#day of the week as an integer, where Monday is 0 and Sunday is 6.
pyday = datetime.datetime.today().weekday()
print "pyday:", pyday

if (pyday <= 5):
	daynow = pyday +2
	nexday = daynow +1
else: 
	daynow = 1
	nexday = 2

print "daynow:", daynow
#f    = open("pacman", "r")
#line = f.readlines()
#curr = line[dayn]

with open('pacman', 'r') as f1, open('pacman.tmp' , 'w') as f2:
	lines = f1.readlines()
#	curr  = lines[dayn]
	poz = 0 #deff value
#	strn= 0
	

	def domagic():
            #print "oldchar", oldchar
	    next_day_char = line[nexday][poz]
	    if  (next_day_char == '.'):
                nextchar = "n"
            elif(next_day_char == 'x'):
		nextchar = "v"
	   	   
	    newline_list  	  = list(lines[(nexday-1)])
	    #print "nextdayl", newline_list
	    newline_list[poz]     = nextchar
	    newstr 		  = "".join(newline_list)	    
	    print newstr
	   # nl = line[nexd].replace('.','n',poz+1)

	for line in lines:
		line = line.strip()
		curr = line[daynow]		
		#print ('curr', curr)	

		if "v" in line and daynow !=7:
			poz = line.find("v")				
			oldchar = "x"		
		        oldline = line.replace('v', 'x')
			print oldline			
           		domagic()
		elif "n" in line:
#			print("no")
			poz = line.find("n")
			oldchar = "."
			oldline = line.replace('n', '.')
		elif (line == daynow + 1):
			continue
		else:
		    print line
		


#curr[poz] = "z"
#		print "today ", curr
#		print "nextd ", newstr
#		print "old   ", oldstr
#		f2.write(oldstr)


#change current

#print "dayn", dayn, line[dayn]
#print "next", nexd, line[nexd], ndc
