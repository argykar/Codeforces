n = int(input())

c1 = n // 100
remain = n % 100
c2 = remain // 20
remain = remain % 20
c3 = remain // 10
remain = remain % 10
c4 = remain // 5
remain = remain % 5
c5 = remain

total = c1 + c2 + c3 + c4 + c5
print(total)