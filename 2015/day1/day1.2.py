#!/usr/bin/env python3

with open('input', 'r') as f:
    content = f.read()

finalResult = 0
i = 0

for i in range(len(content)):
    if content[i] == '(':
        finalResult += 1
    elif content[i] == ')':
        finalResult -= 1
        if finalResult < 0:
            break
print(i+1)
