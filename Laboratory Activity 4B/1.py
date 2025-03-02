# Define the sets
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("Number of elements in A ∪ B:", len(A | B))

print("Number of elements in B - (A ∪ C):", len(B - (A | C)))

print("Set {h, i, j, k}:", C - (A | B))

print("Set {c, d, f}:", A & B & C)

print("Set {b, c, h}:", (A & B) | {'h'})

print("Set {d, f}:", A & C)

print("Set {c}:", A & B & C)

print("Set {l, m, o}:", B - (A | C))
