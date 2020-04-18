k, r = map(int, input().split())
i = 0
while True:
    i += 1
    if (k * i) % 10 == r or (k * i) % 10 == 0:
        break
print(i)
