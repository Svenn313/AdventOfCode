#!/usr/bin/env python3
import copy

ribbon = []
contents = []
wrap = 0
ribboncount = 0

with open("input", "r") as f:
    for line in f:
        line = line.strip().split('x')
        contents.append(line)

ribbon = contents.copy()
for i in range(len(contents)):
    for j in range(len(contents[i])):
        contents[i][j] = int(contents[i][j])
        ribbon[i][j] = copy.copy(contents[i][j])
    ribbon[i].sort()

for i in ribbon:
    ribboncount = ribboncount + (i[0] * 2) + (i[1] * 2) + (i[0]*i[1]*i[2])
print(ribboncount)

for i in contents:
    l = i[0]
    w = i[1]
    h = i[2]
    paper = ((2*l*w) + (2*w*h) + (2*h*l))
    extra = min((l*w),(w*h),(h*l))
    wrap = wrap + paper + extra
print(wrap)
