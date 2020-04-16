n = map(int, input())
word = input()
res = []
for letter in word:
    if 'n' in letter:
        res.append(1)
    elif 'z' in letter:
        res.append(0)

for i in sorted(res, reverse=True):
  print(i, end=' ')