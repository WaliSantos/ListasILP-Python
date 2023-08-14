def insertSort(lista):
    for i in range(1,len(lista)):
        chave = lista[i]
        j = i - 1
        while  j>=0 and lista[j] > chave:
            lista[j +1] = lista[j]
            j-=1
        
        lista[j+1] = chave


n = int(input())
playlist = []
for i in range(0,n):
    s = input()
    playlist.append(s)

insertSort(playlist)

for j in playlist:
    print(j)