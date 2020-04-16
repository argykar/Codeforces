n = int(input())
moves = 0

moves += n // 5
n %= 5
moves += n // 4
n %= 4
moves += n // 3
n %= 3
moves += n // 2
n %= 2
moves += n // 1
n %= 1

print(moves)
