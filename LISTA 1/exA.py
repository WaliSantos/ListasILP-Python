
x = int(input("Entre com o número x de titãs: "))
y= int(x/5 - 4) 

if 20<= x <=200 and x % 5 == 0:
    print("A quantidade de soldados comuns necessários são: ", y)
else:
    print("A quantidade de titãs precisa estar entre 20 e 200 e ser múltiplo de 5!") 