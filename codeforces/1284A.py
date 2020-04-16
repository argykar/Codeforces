n, m = map(int, input().split())

s = input()
s = s.split(' ')
t = input()
t = t.split(' ')

q= int(input())
lista = []
while q:
    x = int(input())
    lista.append(s[(x-1) % n] + t[(x-1) % m])
    q -= 1

for i in lista:
    print(i)
