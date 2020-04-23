import math
n, x, y = map(int, input().split())
clones = math.ceil(y * n  / 100) - x
if clones >= 0:
    print(clones)
else:
    print(0)
