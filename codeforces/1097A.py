hand = input()

table = input().split()

res = 'NO'
for k in table:
    for j in hand:
        if (j in k[0]) | (j in k[1]):
            res = 'YES'
            
print(res)