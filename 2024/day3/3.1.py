#!/usr/bin/env python3
import re
toParse = 0

with open('input','r') as f:
    toParse = f.read()
MultParsed = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)' , toParse)
i = 0
tupleMult = 0
finalResult = 0

for item in MultParsed:
    tupleMult = int(item[0]) * int(item[1])
    finalResult = finalResult + tupleMult

print(finalResult)