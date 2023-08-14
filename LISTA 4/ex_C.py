n = int(input())

enigma = input()
chave = input()

confere = "v"

for a in chave: 
    if enigma.count(a) != chave.count(a): 
        print("Nenhuma informacao util")
        confere = "x"
        break

if confere == "v":
    print("Palavra chave encontrada")


    
    



