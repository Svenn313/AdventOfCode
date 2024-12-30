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

for i in range(len(reports)):
    flag = 0
    croissant = 0
    for j in range(len(reports[i]) - 1):
        level = int(reports[i][j])
        level_plus_un = int(reports[i][j+1])
        if flag == 0:
            if level < level_plus_un and abs(level - level_plus_un) <= 3:
                flag = flag
                if croissant == 0 or croissant == 1:
                     croissant = 1
                else:
                     flag = 1
            elif level > level_plus_un and abs(level - level_plus_un) <= 3:
                flag = flag
                if croissant == 0 or croissant == -1:
                     croissant = -1
                else:
                     flag = 1
            else:
                flag = 1
    if flag == 0:
            okreport += 1
            print(reports[i])
            print(okreport)
    else:
            okreport == okreport
