t = int(input())

for i in range(t):
    a = int(input())
    b = list(map(int, input().split(' ')))

    sum = 0
    odd, even = False, False
    for i in b:
        sum += i
        odd = odd | (i % 2 == 0)
        even = even | (i % 2 != 0)
    if (sum % 2 != 0 or (odd and even)):
        print('YES')
    else:
        print('NO')
