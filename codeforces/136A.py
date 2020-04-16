n = int(input())
p_i = list(map(int, input().split(' ')))
arr = []
for i in p_i:
    arr.append(i)

for i in range(1, n+1):
    print(arr.index(i) + 1, end=' ')
