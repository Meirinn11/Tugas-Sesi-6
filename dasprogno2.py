def print_number_pattern(rows):
    for i in range(1, rows + 1):
        num = i
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

print_number_pattern(5)