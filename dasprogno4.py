def print_number_pattern(rows, columns):
    for i in range(1, rows + 1):
        num = i
        for j in range(columns):
            print(num, end=" ")
            num += 2
        print()

rows = 5
columns = 5
print_number_pattern(rows, columns)