n = int(input())
l = []

for i in range(1, n):
	if n % i == 0:
		l.append(i)
	else:
		continue

print(len(l))