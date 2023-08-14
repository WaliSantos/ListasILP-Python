def buscaBin(x,k):
    a = 0
    b = len(x)-1
    
    while a<= b:
        i = int((a+b)//2)
        if int(x[i]) == k:
            return i
        elif int(x[i]) < k:
            a = i + 1
        else:
            b = i - 1
    
    return

c = int(input())

for i in range(0,c):
    n = int(input())
    t = input().split()
    k = int(input())
    print(int(buscaBin(t,k)))
    
    
    