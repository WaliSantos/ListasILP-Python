n, m = input().split()
n= int(n)
m = int(m)
matriz = []
cont = 0

for q in range(0,n):
    c = input().split()
    matriz.append(c)

for u in range(0,m):
    l, c = input().split()
    c = int(c)
    l = int(l)
    for j in range(0,n):
        if j == c:
            for i in range(l-1,0,-1):
                if matriz[i][j]=="1":
                    cont += 1
                    break
            

print(cont)
        
