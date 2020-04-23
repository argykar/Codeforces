n = int(input())
t = list(map(int, input().split()))

zeros = 0
fives = 0
for i in t:
    if i == 5:
        fives += 1
    else:
        zeros += 1

if zeros == 0:
    print(-1)
elif fives < 9:
    print(0)
else:
    while sum(t) % 9 != 0:
        t.remove(5)
    for i in sorted(t, reverse=True):
        print(i, end='')
