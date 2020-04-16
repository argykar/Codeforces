n = int(input())
for i in range(n):
    s = input()
    if s.endswith('po'):
        print('FILIPINO')
    elif s.endswith('desu') or s.endswith('masu'):
        print('JAPANESE')
    else:
        print('KOREAN')
