s, n = input().split()
s = int(s)
n = int(n)

a = [0]*n

for x in range(1,s+1):
    p = int(input())
    for i in range(0,n,p):
        a[i] = 1

print(*a)