def insertSort(x):
    for i in range(3,len(x),2):
        chave = x[i]
        j = i-2
        while j>=0 and x[j]> chave:
            x[j+2]= x[j]
            j-=2
        x[j+2] = chave



n = int(input())
aprovados = []
for i in range(0,n):
    m,c = input().split()
    m = int(m)
    aprovados.append(m)
    aprovados.append(c)

insertSort(aprovados)

for j in range(1,len(aprovados),2):
    print(aprovados[j],aprovados[len(aprovados)-2*j])

