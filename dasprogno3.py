#1 2 3 4 5 
#2 3 4 5 
#3 4 5 
#4 5 
#5 
def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows + 1):
            print(j, end=" ")
        print()

print_number_pattern(5)
