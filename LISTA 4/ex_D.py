n = int(input())
l = input().split()

cont = 0

for i in range(0,n):
  if cont == 0:
    for j in range(i+1,n):
      if l[i] == l[j]:
        print(int(l[i]))
        cont += 1
        break

if cont == 0:
  print(-1)
