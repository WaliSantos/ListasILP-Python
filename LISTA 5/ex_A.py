def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def buscaBin(x,k):
    a = 0
    b = len(x)-1

    while a <= b:
        i = int((a+b)//2)
        if int(x[i][0]) == k:
            return f'{x[i][2]}: {x[i][1]}'
        elif int(x[i][0]) < k:
            a = i + 1
        else:
            b = i - 1
    return "Aluno nao encontrado"

n = int(input())
acumula = []
for i in range(0,n):
    x = input().split()
    acumula.append(x)

insertion_sort(acumula)

c = int(input())

for j in range(0,c):
    m = int(input())
    print(buscaBin(acumula,m))