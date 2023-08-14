n = int(input())

acumulaG = 0
acumulaT = 0

for i in range(1,n+1):
    pedido = int(input())
    if(pedido == 11):
        acumulaG = acumulaG + 1
    elif(pedido == 10):
        acumulaT = acumulaT + 1
if(acumulaG >= acumulaT):
    print("Geleia")
else:
    print("Tradicional")