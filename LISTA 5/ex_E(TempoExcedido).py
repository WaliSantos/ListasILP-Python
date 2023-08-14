def insertSort(x):
    for i in range(1,len(x)):
        chave = x[i]
        j = i-1
        while j>=0 and  int(x[j]) > int(chave):
            x[j+1]= x[j]
            j-=1
        x[j+1] = chave
    
lista = []
while True:
    try: 
        d,m,a = input().split()
        d = int(d)
        m = int(m)
        a = int(a)

        d = f'{d:02}'
        m = f'{m:02}'
        a = f'{a:04}'
       
        d = str(d)
        m = str(m)
        a = str(a)

        lista.append(a+m+d)
        
    except:
        break
    
insertSort(lista)

for j in range(0,len(lista)):
    print(int(lista[j][6:8]),int(lista[j][4:6]),int(lista[j][0:4])) #aaaammdd 