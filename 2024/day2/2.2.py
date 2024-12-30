#!/usr/bin/env python3

reports = [[]]

with open("input", "r") as f:
    for line in f:
        line = line.strip()
        elements = line.split()
        reports.append(elements)
reports.pop(0)

i = 0
j = 0
okreport = 0
level = reports[i][j]
level_plus_un = reports[i][j+1]

def check(line):
    unsafe = False
    croissant = 0
    for j in range(len(line) - 1):
        level = int(line[j])
        level_plus_un = int(line[j+1])
        if abs(level - level_plus_un) > 3 :
            unsafe = True
            break
        if level < level_plus_un:
            if croissant == 0 or croissant == 1:
                croissant = 1
            else:
                unsafe = True
                break
        elif level > level_plus_un:
            if croissant == 0 or croissant == -1:
                croissant = -1
            else:
                unsafe = True
                break
        else:
            unsafe = True
            break
    return unsafe

for i in range(len(reports)):
    isMyLaneUnsafe = check(reports[i])
    if isMyLaneUnsafe == False:
        okreport += 1
    else:
        reports_copy = reports[i].copy()
        for j in range(len(reports[i])):
            toUnpop = reports_copy[j]
            reports_copy.pop(j)
            isMyLaneUnsafe = check(reports_copy)
            if isMyLaneUnsafe == False:
                okreport += 1
                break
            else:
                reports_copy.insert(j,toUnpop)

print ("okreports : %d" % okreport)
