n,q = input().split()
n = int(n)
q= int(q)

soma = 0
i=1

while (i < n):
    soma = soma + q*2**i
    i = i + 1

print(q + soma)