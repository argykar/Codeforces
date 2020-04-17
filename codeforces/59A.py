s = input()
upper = 0
lower = 0

for i in s:
    if i == i.lower():
        lower += 1
    else:
        upper += 1
if lower == upper or lower > upper:
    s = s.lower()
else:
    s = s.upper()

print(s)
