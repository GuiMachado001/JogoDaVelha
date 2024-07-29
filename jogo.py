import random

matriz =[[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]
         ]

def printJogo(jogada):
    print("   0   1  2")
    print("0- __|__|__ \n1- __|__|__ \n2-   |  |  ")
printJogo
def jogadaMaquina ():
    geradorJogada = random.randrange(1, 90)

    if(geradorJogada <=5):
        if(matriz[0][0] == 1):
            return jogada
        else:
            matriz[0][0] == 1

    elif(geradorJogada > 5 and geradorJogada <= 10):
        if(matriz[0][1] == 1):
            return jogada
        else:
            matriz[0][1] == 1

    elif(geradorJogada > 10 and geradorJogada <= 15):
        if(matriz[0][2] == 1):
            return jogada
        else:
            matriz[0][2] == 1

    elif(geradorJogada > 15 and geradorJogada <= 20):
        if(matriz[1][0] == 1):
            return jogada
        else:
            matriz[1][0] == 1

    elif(geradorJogada > 20 and geradorJogada <= 25):
        if(matriz[1][1] == 1):
            return jogada
        else:
            matriz[1][1] == 1

    elif(geradorJogada > 20 and geradorJogada <= 25):
        if(matriz[1][2] == 1):
            return jogada
        else:
            matriz[1][2] == 1

    elif(geradorJogada > 25 and geradorJogada <= 30):
        if(matriz[2][0] == 1):
            return jogada
        else:
            matriz[2][0] == 1

    elif(geradorJogada > 25 and geradorJogada <= 30):
        if(matriz[2][1] == 1):
            return jogada
        else:
            matriz[2][1] == 1

    elif(geradorJogada > 25 and geradorJogada <= 30):
        if(matriz[2][2] == 1):
            return jogada
        else:
            matriz[2][2] == 1
print00 = "__ |"
print01 = "__ |"
print02 = "__"

print10 = "__ |"
print11 = "__ |"
print12 = "__"

print20 = "   |"
print21 = "   |"
print22 = "  "

primeiroJogador = random.randrange(1, 6)

if(primeiroJogador <= 3):
    matriz[0][0] = 1
    print00 =  'x |'

print(primeiroJogador)
print(print00,print01,print02)
print(print10,print11,print12)
print(print20,print21,print22)

while True:
    jogadaMaquina
    jogada = input(f"Digite a sua jogada (linha, coluna): ")
    linha, coluna = jogada.split(',')
    
    print(linha, coluna)

    linha = int(linha)
    coluna = int(coluna)
    
    matriz[linha][coluna] = 1
    
    
    if(linha == 0 and coluna == 0):
        print00 = " x |"
    elif(linha == 0 and coluna == 1):
        print01 = " x |"
    elif(linha == 0 and coluna == 2):
        print02 = "x "

    elif(linha == 1 and coluna == 0):
        print10 = " x |"
    elif(linha == 1 and coluna == 1):
        print11 = " x |"
    elif(linha == 1 and coluna == 2):
        print12 = "x "

    elif(linha == 2 and coluna == 0):
        print20 = " x |"
    elif(linha == 2 and coluna == 1):
        print21 = " x |"
    elif(linha == 2 and coluna == 2):
        print22 = "x "

    print(print00,print01,print02)
    print(print10,print11,print12)
    print(print20,print21,print22)

    print(matriz)

    if(matriz[0][0] == 1 and matriz[0][1] == 1 and matriz[0][2] == 1): ##Vitoria linha 0 Horizontal
        print('Você Ganhou !!!')
    elif(matriz[1][0] == 1 and matriz[1][1] == 1 and matriz[1][2] == 1): ##Vitoria linha 1 Horizontal
        print('Você Ganhou !!!')
    elif(matriz[2][0] == 1 and matriz[2][1] == 1 and matriz[2][2] == 1):##Vitoria linha 2 Horizontal
        print('Você Ganhou !!!')
    elif(matriz[0][0] == 1 and matriz[1][0] == 1 and matriz[2][0] == 1):##Vitoria linha 0 Vertical
        print('Você Ganhou !!!')
    elif(matriz[0][1] == 1 and matriz[1][1] == 1 and matriz[2][1] == 1):##Vitoria linha 1 Vertical
        print('Você Ganhou !!!')
    elif(matriz[0][2] == 1 and matriz[1][2] == 1 and matriz[2][2] == 1):##Vitoria linha 2 Vertical
        print('Você Ganhou !!!')
    elif(matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[2][2] == 1):##Vitoria Diagonal
        print('Você Ganhou !!!')
    elif(matriz[0][2] == 1 and matriz[1][1] == 1 and matriz[2][0] == 1):##Vitoria Diagonal
        print('Você Ganhou !!!')
    


# print(lineOne)
# print(lineTwo)
# print(linetree)

