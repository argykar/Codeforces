n = int(input())
arr =[]
for i in range(n):
    m = input()
    arr.append(m)

groups = 1

for i in range(1, len(arr)):
    if arr[i-1][1] == arr[i][0]:
        groups += 1

print(groups)
