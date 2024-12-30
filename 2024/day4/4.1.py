#!/usr/bin/env python3

matrice = []
i = 0
j = 0
finalResult = 0

def check_horizontal():
    okWord = 0
    if j+3 < len(matrice[i]) and matrice[i][j+1] == "M" and matrice[i][j+2] == "A" and matrice[i][j+3] == "S" :
                okWord += 1
    if j-3 >= 0 and matrice[i][j-1] == "M" and matrice[i][j-2] == "A" and matrice[i][j-3] == "S" :
                okWord += 1
    return okWord

def check_vertical():
    okWord = 0
    if i+3 < len(matrice) and matrice[i+1][j] == "M" and matrice[i+2][j] == "A" and matrice[i+3][j] == "S" :
                okWord += 1
    if i-3 >= 0 and matrice[i-1][j] == "M" and matrice[i-2][j] == "A" and matrice[i-3][j] == "S":
                okWord += 1
    return okWord

def check_diagonal():
    okWord = 0
    # en bas a droite
    if j+3 < len(matrice[i]) and i+3 < len(matrice) and matrice[i+1][j+1] == "M" and matrice[i+2][j+2] == "A" and matrice[i+3][j+3] == "S" :
        okWord += 1
    # en haut a droite
    if j+3 < len(matrice[i]) and i-3 >= 0 and matrice[i-1][j+1] == "M" and matrice[i-2][j+2] == "A" and matrice[i-3][j+3] == "S" :
        okWord += 1
    # en bas a gauche
    if j-3 >= 0 and i+3 < len(matrice) and matrice[i+1][j-1] == "M" and matrice[i+2][j-2] == "A" and matrice[i+3][j-3] == "S" :
        okWord += 1
    # en haut a gauche
    if j-3 >= 0 and i-3 >= 0 and matrice[i-1][j-1] == "M" and matrice[i-2][j-2] == "A" and matrice[i-3][j-3] == "S" :
        okWord += 1
    return okWord


with open('input','r') as f:
    matrice = f.read().splitlines()

for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        charCheck = matrice[i][j]
        if charCheck == "X":
            finalResult += check_horizontal()
            finalResult += check_vertical()
            finalResult += check_diagonal()

print(finalResult)

