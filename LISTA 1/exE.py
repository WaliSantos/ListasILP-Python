
q1 = int(input("Quantidade de ovos coletados na primeira caçada: "))
q2 = int(input("Quantidade de ovos coletados na segunda caçada: "))
q3 = int(input("Quantidade de ovos coletados na terceira caçada: "))

e1 = int(input("Quantidade de ovos envenenados na primeira caçada: "))
e2 = int(input("Quantidade de ovos envenenados na segunda caçada: "))
e3 = int(input("Quantidade de ovos envenenados na terceira caçada: "))

ovosQueSobraram = (q1 - (e1*2 + e1)) + (q2 - (e2*2 + e2)) + (q3 - (e3*2 + e3))

print(ovosQueSobraram)


