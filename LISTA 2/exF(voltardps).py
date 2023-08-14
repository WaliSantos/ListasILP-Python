a,m,c= input().split()
a = int(a)
m = int(m)
c = int(c)

qtdA = a//2
qtdM = m//3
qtdC = c//5

quantidade = 0

if qtdA <= qtdM and qtdA <= qtdC:
    quantidade = qtdA
   
if qtdM <= qtdA and qtdM <= qtdC:
    quantidade = qtdM
    
if qtdC <= qtdA and qtdC <= qtdM:
    quantidade = qtdC
    

print(quantidade)




