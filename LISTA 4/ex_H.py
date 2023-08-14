
matriz = []
for p in range(0,8):
    linha = input().split()
    matriz.append(linha)

x,y = input().split()
x=int(x)
y=int(y)

inimigo = 0

for i in range(x-1,-1,-1):
    if matriz[i][y] == "2":
        inimigo += 1
        break
    elif matriz[i][y] == "1":
        break

for i in range(x+1,8):
    if matriz[i][y] == "2":
        inimigo += 1
        break
    elif matriz[i][y] == "1":
        break

for i in range(y-1,-1,-1):
    if matriz[x][i] == "2":
        inimigo += 1
        break
    elif matriz[x][i] == "1":
        break

for i in range(y+1,8):
    if matriz[x][i] == "2":
        inimigo += 1
        break
    elif matriz[x][i] == "1":
        break

print(inimigo)

