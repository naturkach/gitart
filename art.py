#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

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

if os.path.exists("pacman.tmp"):
    os.remove("pacman.tmp")

#f    = open("pacman", "r")
#line = f.readlines()
#curr = line[dayn]

with open('pacman', 'r') as f1, open('pacman.tmp' , 'w') as f2:
	lines = f1.readlines()
	poz = 0 #deff value	

	def domagic():
	    next_day_char = line[nexday][poz]
	    if  (next_day_char == '.'):
                nextchar = "n"
            elif(next_day_char == 'x'):
		nextchar = "v"
	   	   
	    newline_list  	  = list(lines[(nexday-1)])
	    newline_list[poz]     = nextchar
	    newstr = "".join(newline_list)
	    newstr = newstr.rstrip()	    	    
#	    print (newstr)
	    f2.write(newstr)
	    f2.write("\n")

	for line in lines:
		line = line.strip()
		curr = line[daynow]		
		#print ('curr', curr)	

		if "v" in line and daynow !=7:
			poz = line.find("v")				
			oldchar = "x"		
		        oldline = line.replace('v', 'x')
			print oldline
			f2.write(oldline)
			f2.write("\n")					
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
	            f2.write(line)
		    f2.write("\n")
		

f1.close()
f2.close()

#curr[poz] = "z"
#		print "today ", curr
#		print "nextd ", newstr
#		print "old   ", oldstr
#		f2.write(oldstr)


#change current

#print "dayn", dayn, line[dayn]
#print "next", nexd, line[nexd], ndc
