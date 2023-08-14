n1,n2,n3,n4,n5,n6 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

soma= n1 + n2 + n3 + n4 + n5 + n6

if(soma>=250):
    print("S+")
elif(soma>=200):
    print("S")
elif(soma>=180):
    print("S-")
elif(soma>=150):
    print("A+")
elif(soma>=100):
    print("A")
elif(soma>=80):
    print("A-")
elif(soma>=60):
    print("B+")
elif(soma>=40):
    print("B")
elif(soma>=39):
    print("B-")

