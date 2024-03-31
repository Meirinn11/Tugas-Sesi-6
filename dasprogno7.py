#A B A B A
#B A B A B
#A B A B A
#B A B A B

row = 4
col = 5
karakter = ['A', 'B']

for r in range(row):
    for j in range(col):
        print(karakter[(r + j) % 2], end=" ")
    print()