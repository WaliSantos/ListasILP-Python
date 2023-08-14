n = int(input())

matriz = []
for p in range(0,n):
    linha = input().split()
    matriz.append(linha)

c = int(input())

soma =0
for a in range(0,c):
    x,y = input().split()
    x = int(x)
    y = int(y)
    soma += int(matriz[x][y])

print(soma)


