t = int(input())
acumulaP = 0
p = ""
while(p!=0):
    p = int(input())
    if(p>t):
        acumulaP = p
if(acumulaP>t):
    print("ALARME")
else:
    print("O Havai pode dormir tranquilo")