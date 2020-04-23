t = int(input())
for rew in range(t):
	n = int(input())
	if n%4 == 2:
		print("NO")
	else:
		print("YES")
		n//=2
		even = [2*(i+1) for i in range(n)]
		odd = [2*i+1 for i in range(n-1)]
		diff = sum(pocz)-sum(kon)
		res = even + odd + [diff]
		print(*res)
