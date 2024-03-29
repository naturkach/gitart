#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

# day of the week as an integer, where Monday is 0 and Sunday is 6.
# but:
# 0123456 - py_day
# 1234567 - normal_day (line_number)
# 7123456 - git_day

pyday = datetime.datetime.today().weekday()
print("pyday:", pyday)
print("home", os.environ['HOME'])
fpath = (os.environ['HOME']) + "/gitart/"
print("path:", fpath)

if (pyday < 6):
    daynow = pyday + 1
    nexday = daynow + 1
else:
    daynow = pyday + 1
    nexday = 1

print("daynow:", daynow)
print("nexday:", nexday)

if os.path.exists(fpath + "pacman.tmp"):
    os.remove(fpath + "pacman.tmp")

commit = "no"

# with open(fpath+"pacman", 'r') as f1, open(fpath+"pacman.tmp" , 'w') as f2:
with open("pacman", 'r') as f1, open("pacman.tmp", 'w') as f2:
    lines = f1.readlines()
    poz = 0  # deff value
    linenumb = 1


    def domagic():
        #        print ("line:", lines[nexday][poz])

        next_day_char = lines[nexday][poz]

        if (next_day_char == '.'):
            nextchar = "n"
        elif (next_day_char == 'x'):
            nextchar = "v"

        newline_list = list(lines[(nexday)])
        newline_list[poz] = nextchar
        newstr = "".join(newline_list)
        newstr = newstr.rstrip()
        print(linenumb, newstr)
        f2.write(newstr)
        f2.write("\n")


    for line in lines:
        line = line.strip()
        # curr = line[daynow]

        if "v" in line and daynow != 7:
            poz = line.find("v")
            oldchar = "x"
            oldline = line.replace('v', 'x')
            print(linenumb, oldline)
            linenumb + 1
            f2.write(oldline)
            f2.write("\n")
            domagic()
            linenumb += 1
            commit = "yes"

        elif "n" in line:
            poz = line.find("n")
            oldchar = "."
            oldline = line.replace('n', '.')
            linenumb += 2
            commit = "no"
        elif linenumb == nexday + 1:
            linenumb += 1
        else:
            print(linenumb, line)
            f2.write(line)
            f2.write("\n")
            linenumb += 1

if commit == "yes":
    os.chdir(fpath)
    os.system("mv pacman.tmp pacman")
    os.system("git add .")
    os.system("git commit -m \"auto commit\"")
    os.system("git push")

f1.close()
f2.close()
