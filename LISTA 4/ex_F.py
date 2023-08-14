n = int(input()) #tamanho da plantação NxN
matriz = []
for p in range(0,n):
    linha = input().split()
    matriz.append(linha)

somaH = 0
somaR = 0


x, y = input().split()
x = int(x)
y = int(y)

for j in range (0,n):
    somaH += int(matriz[x][j])

for i in range (0,n):
    somaR += int(matriz[i][y])

if ((n-1) - y) > ((n-1) - x):
    somaR -= int(matriz[x][y])

elif ((n-1) - y) <= ((n-1) - x):
    somaH -= int(matriz[x][y])
    
print("Harry", somaH )
print("Ron", somaR)