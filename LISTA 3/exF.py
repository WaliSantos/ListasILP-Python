
acumulaCor=""
cor =""
v = "vermelho"
am = "amarelo"
az = "azul"
vd = "verde"
p = "preto"
b = "branco"

while(cor!=b and cor!=p):
    cor = input()
    acumulaCor = acumulaCor + cor
    if(acumulaCor == v + az 
       or acumulaCor == az + b):
        print("roxo")
        acumulaCor = ""
    elif(acumulaCor == am + b
         or acumulaCor == vd + vd):
        print("verde")
        acumulaCor = ""
    elif(acumulaCor == az + vd):
        print("ciano")
        acumulaCor = ""
    elif(acumulaCor == am + vd):
        print("lima")
        acumulaCor = ""
    elif(acumulaCor == v + vd):
        print("marrom")
        acumulaCor = ""
    elif(acumulaCor == v + v):
         print("vermelho")
         acumulaCor = ""
    elif(acumulaCor == am + am):
         print("amarelo")
         acumulaCor = ""
    elif(acumulaCor == az + az):
         print("azul")
         acumulaCor = ""
    
if(cor == p):
    print("Game Over")



