#4)
#1 3 5 7 9
#2 4 6 8 10
#3 5 7 9 11
#4 6 8 10 12
#5 7 9 11 13
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
