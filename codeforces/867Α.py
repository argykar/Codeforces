n = map(int, input())
s = input()
f = s
s = s.split('SF')
f = f.split('FS')

if len(s) > len(f):
    print('YES')
else:
    print('NO')
