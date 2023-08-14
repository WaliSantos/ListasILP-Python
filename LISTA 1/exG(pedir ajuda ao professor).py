n = int(input("Tempo em segundos: "))
hora = int(n/3600)
minutos = int((n%3600)/60)
segundos = int((n%3600)%60)


  
print(str(hora)+"h", str(minutos)+"m", str(segundos)+"s")