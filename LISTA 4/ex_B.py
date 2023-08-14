n = int(input())
a = input().split()
m = int(input())
l = 0
l= m

for i in range(0,len(a)):
    while l>0:
        if int(a[i])>1 or int(a[i])==0:
            l = l - int(a[i])
        else:
            l = m
        break

if l >0:   
    print("Yes, you can")
else:
    print("You Died")
    


    