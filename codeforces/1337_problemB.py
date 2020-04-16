t = int(input())
for i in range(t):
    x, n, m = map(int, input().split())
    if  x - (m * 10) <= 0:
        print('YES')
    else:
        for i in range(n):
            x = x // 2 + 10
        if  x - (m * 10) <= 0:
            print('YES')
        else:
            print('NO')
