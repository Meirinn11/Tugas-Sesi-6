def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows + 1):
            print(j, end=" ")
        print()

print_number_pattern(5)