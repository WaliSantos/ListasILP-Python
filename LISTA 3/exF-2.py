
cor = input()
cor2= ""

v = "vermelho"
am = "amarelo"
az = "azul"
vd = "verde"
p = "preto"
b = "branco"

while(cor!="branco" and cor!="preto"):
    cor2 = input()
    if(cor == cor2):
        print(cor2)
    elif((cor == v and cor2==az)
         or (cor == az and cor2==v)):
        print("roxo")
    elif((cor == az and cor2==am)
         or (cor == am and cor2==az)):
        print("verde")
    elif((cor == az and cor2==vd)
         or (cor == vd and cor2==az )):
        print("ciano")
    elif((cor == am and cor2==vd)
         or (cor == vd and cor2==am)):
        print("lima")
    elif((cor == v and cor2==vd)
         or (cor == vd and cor2==v)):
        print("marrom")
    elif((cor == v and cor2==am)
         or (cor == am and cor2==v)):
        print("laranja")
    cor = cor2
if(cor == p):
    print("Game Over")