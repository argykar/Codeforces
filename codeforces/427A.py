n = int(input())
arr = list(map(int, input().split(' ')))
police, crimes = 0, 0

for i in arr:
    if i > 0:
        police += i
        continue
    if police > 0 and i < 0:
        police -= 1
        continue
    if i < 0:
        crimes += 1

print(crimes)
