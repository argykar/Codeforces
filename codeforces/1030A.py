n = int(input())
k = map(int, input().split())

if sum(k) == 0:
    print('easy')
else:
    print('hard')
