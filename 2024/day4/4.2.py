#!/usr/bin/env python3

matrice = []
i = 0
j = 0
finalResult = 0

def check_MAS():
    okWord = 0
    if  j+1 < len(matrice[i]) and i+1 < len(matrice) and matrice[i+1][j+1] == "M" and \
        j+1 < len(matrice[i]) and i-1 >= 0 and matrice[i-1][j+1] == "S" and \
        j-1 >= 0 and i+1 < len(matrice) and matrice[i+1][j-1] == "M" and \
        j-1 >= 0 and i-1 >= 0 and matrice[i-1][j-1] == "S":
        okWord += 1    
    if  j+1 < len(matrice[i]) and i+1 < len(matrice) and matrice[i+1][j+1] == "S" and \
        j+1 < len(matrice[i]) and i-1 >= 0 and matrice[i-1][j+1] == "M" and \
        j-1 >= 0 and i+1 < len(matrice) and matrice[i+1][j-1] == "S" and \
        j-1 >= 0 and i-1 >= 0 and matrice[i-1][j-1] == "M":
        okWord += 1
    if  j+1 < len(matrice[i]) and i+1 < len(matrice) and matrice[i+1][j+1] == "M" and \
        j+1 < len(matrice[i]) and i-1 >= 0 and matrice[i-1][j+1] == "M" and \
        j-1 >= 0 and i+1 < len(matrice) and matrice[i+1][j-1] == "S" and \
        j-1 >= 0 and i-1 >= 0 and matrice[i-1][j-1] == "S":
        okWord += 1
    if  j+1 < len(matrice[i]) and i+1 < len(matrice) and matrice[i+1][j+1] == "S" and \
        j+1 < len(matrice[i]) and i-1 >= 0 and matrice[i-1][j+1] == "S" and \
        j-1 >= 0 and i+1 < len(matrice) and matrice[i+1][j-1] == "M" and \
        j-1 >= 0 and i-1 >= 0 and matrice[i-1][j-1] == "M":
        okWord += 1
    return okWord

with open('input','r') as f:
    matrice = f.read().splitlines()

for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        charCheck = matrice[i][j]
        if charCheck == "A":
            finalResult += check_MAS()

print(finalResult)