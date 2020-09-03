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

if "v" in curr:
	print("ok")
	poz = curr.find("v")
	print (poz)
	#git commit

#get nextday char:
ndc = line[nexd][poz]

if (ndc == '.'):
	nl = line[nexd].replace('.','n',1)

print "nl=", nl

print "dayn", dayn, line[dayn]
print "next", nexd, line[nexd], ndc, line[nexd][poz]
