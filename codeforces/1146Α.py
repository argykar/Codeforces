s = input()
counter_a = 0
counter_else = 0

for i in s:
    if 'a' == i:
        counter_a += 1
    else:
        counter_else += 1

s_len = len(s)
while counter_a <= counter_else:
    s_len -= 1
    counter_else -= 1

print(s_len)
