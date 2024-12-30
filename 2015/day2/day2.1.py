#!/usr/bin/env python3

contents = []
wrap = 0

with open("input", "r") as f:
    for line in f:
        line = line.strip().split('x')
        contents.append(line)

for i in range(len(contents)):
    for j in range(len(contents[i])):
        contents[i][j] = int(contents[i][j])

for i in contents:
    l = i[0]
    w = i[1]
    h = i[2] 
    paper = ((2*l*w) + (2*w*h) + (2*h*l))
    extra = min((l*w),(w*h),(h*l))
    wrap = wrap + paper + extra
    print(wrap)