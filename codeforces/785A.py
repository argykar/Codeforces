n = int(input()) # the number of polyhedrons
polihedra = {'Tetrahedron' : 4, 
            'Cube' : 6, 
            'Octahedron' : 8, 
            'Dodecahedron' : 12, 
            'Icosahedron' : 20}
edra = []
sum = 0
for i in range(n+1):
    edra.append(input())
    if i == n - 1:
        break
for onoma, edres in polihedra.items():
    for i in edra:
        if i == onoma:
            sum = sum + edres
print(sum)
