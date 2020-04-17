n = int(input())
p = list(map(int, input().split()))

for i in p:
    i /= 100
print(sum(p) / n)
