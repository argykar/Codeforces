w_limak, w_bob = map(int, input().split())
year = 0

while w_limak <= w_bob:
    w_limak = 3 * w_limak
    w_bob = 2 * w_bob
    year +=1
    if w_limak > w_bob:
        break
print(year)
