x1, x2, x3, x4 = map(int, input().split())

lista = [x1, x2, x3, x4]
lista = sorted(lista, reverse=True)

for i in range(len(lista)):
    print(max(lista) - lista[i+1], max(lista) - lista[i+2], max(lista) - lista[i+3])
    break