#!/usr/bin/env python3

valGauche = []
valDroite = []
finalResult = 0

with open("input", "r") as f:
    for line in f:
        line = line.strip()
        elements = line.split()
        if len(elements) == 2:
            valGauche.append(int(elements[0]))
            valDroite.append(int(elements[1]))
valGauche.sort()
valDroite.sort()

x = 0
while x < len(valGauche):
    compte = valDroite.count(valGauche[x])
    similarity = compte * valGauche[x]
    finalResult = finalResult + similarity
    x += 1
    print("x", x)
    print("compte :" , compte)
    print("similarity :", similarity)
    print("finalresult :" ,finalResult)
