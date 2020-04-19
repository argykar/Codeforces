a, b, c = map(int, input().split()) # a = d1, b = d2, c = d3
cost = 0

routes = [2 * b + 2 * c, a + c + b, 2 * a + 2 * b, 2 * a + 2 * c]
print(min(routes))
