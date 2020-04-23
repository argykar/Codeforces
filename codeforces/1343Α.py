t = int(input())
for i in range(t):
    a = int(input())
    k = 2
    while k:
        x = a / (pow(2, k) -1)
        if x != int(x):
            k += 1
            continue
        else:
            print(int(x))

        break
