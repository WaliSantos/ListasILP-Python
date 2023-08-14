
hf =""
hdf=""
ha =""

resultado = "DERROTA"
while (hf!="FIM" and hdf!="FIM" and ha!="FIM"):
    hf,hdf,ha = input().split()
    if(hf=="NAO" and hdf=="SIM" and ha=="NAO"):
        resultado = "VITORIA" 
   
print(resultado)
    