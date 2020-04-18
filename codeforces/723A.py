coords = list(map(int, input().split()))
coords = sorted(coords)
half = coords[1]
res = 0
for i in coords:
    if i == half:
        continue
    else:
        res += abs(half - i)

print(res)
