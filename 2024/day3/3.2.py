#!/usr/bin/env python3
import re
toParse = 0

with open('input','r') as f:
    toParse = f.read()

MultParsed = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)' , toParse)
doParsed = re.finditer(r'(do\(\))' , toParse)
dontParsed = re.finditer(r'(don\'t\(\))' , toParse)
parsedText = []
parsedResult = 0
finalResult = 0

for item in doParsed:
    parsedText.append([item.start(), item.group(1)])
for item in dontParsed:
    parsedText.append([item.start(), item.group(1)])
for item in MultParsed:
    parsedText.append([item.start(), item.group(1), item.group(2)])

parsedText.sort()

flag = 1
for item in parsedText:
    if item[1] == "do()":
        flag = 1
    elif item[1] == "don't()":
        flag = 0
    else:
        if flag == 1:
            parsedResult = int(item[1]) * int(item[2])
            finalResult = finalResult + parsedResult

print(finalResult)