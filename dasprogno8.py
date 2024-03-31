#8)

row = 5
karakter = ['S', 'O']

for r in range(row):
    for j in range(row - r):
        print(karakter[(r + j) % 2], end=" ")
    print()