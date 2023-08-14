def buscaBin (x,k):
    a = 0
    b = len(x) - 1
    while a <= b:
        i = int((a +b)//2)
        if x[i] == k:
            return "Geral"
        elif x[i] < k:
            a = i + 1
        else:
            b = i - 1
    return "Proibido"


n = int(input())
g = input().split()
m = int(input())
p = input().split()

c= int(input())
amostra = input().split()

for i in range(0,c):
    k = amostra[i]
    print(buscaBin(g,k,))


