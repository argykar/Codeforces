n, m = map(int, input().split())
time = []
for i in range(1,n+1):
    time.append(i * 5)

while sum(time) + m > 240:
    time.pop()
else:
    print(len(time))
