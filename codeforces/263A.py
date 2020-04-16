lista = []
for i in range(5):
    inp = map(int, input().split(' '))
    lista.append(list(inp))

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
