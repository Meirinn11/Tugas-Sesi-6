#6)
#+ + + + 5
#+ + + 4 5
#+ + 3 4 5
#+ 2 3 4 5
#1 2 3 4 5
row = 5
col = 5

for r in range(row, 0, -1):
    for j in range(1, col + 1):
        if j < r:
            print("+", end=" ")
        else:
            print(j, end=" ")
    print()