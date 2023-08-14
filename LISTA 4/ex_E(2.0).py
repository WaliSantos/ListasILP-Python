n, m = input().split()
n= int(n)
m = int(m)
matriz = []
destroi = 0

for q in range(0,n):
    c = input().split()
    matriz.append(c)

for u in range(0,m):
    l, c = input().split()
    c = int(c)
    l = int(l)
    
    if  matriz[l][c]!="1":
        for i in range(l-1,-1,-1):
            if matriz[i][c]=="1":
                destroi += 1
                matriz[i][c] = "0"
                break
            

print(destroi)