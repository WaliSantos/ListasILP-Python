def quick_sort(x):
        if len(x) <= 1:
            return x
        else:
            pivô = x[0]
            esquerda = [a for a in x[1:] if a <= pivô]
            direita = [a for a in x[1:] if a > pivô]
            return quick_sort(esquerda) + [pivô] + quick_sort(direita)

lista = []
while True:
    try: 
        d,m,a = input().split()
        d = int(d)
        m = int(m)
        a = int(a)

        listaAx = []
        listaAx.append(a)
        listaAx.append(m)
        listaAx.append(d)

        lista.append(listaAx)
    except:
        break
    
lista = quick_sort(lista)

for j in range(0,len(lista)):
    print(lista[j][2],lista[j][1],lista[j][0]) #aaaammdd 