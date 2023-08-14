def insertSort(x):
    for i in range(1,len(x)):
        chave1 = x[i]
        chave2 = x[i][1]
        j = i-1
        while j>=0 and x[j][1] > chave2:
            x[j+1]= x[j]
            j-=1
        x[j+1] = chave1

n = int(input())
aprovados = []
for i in range(0,n):
    m,c = input().split()
    m = int(m)
    listaAx= []
    listaAx.append(m)
    listaAx.append(c)
    aprovados.append(listaAx)
insertSort(aprovados)

for j in range(0,len(aprovados)):
    print(aprovados[j][1],aprovados[j][0])