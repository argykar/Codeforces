n = int(input())
lista = [int(input()) for i in range(n)]

for j in lista:
  if j == 2:
    print(2)
  elif j % 2 == 0 and j >2:
    print(0)
  else:
    print(1)