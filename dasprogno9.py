fib_sequence = [0, 1]
fib_limit = 10  # Ubah sesuai dengan jumlah angka Fibonacci yang ingin Anda gunakan

# Membangun deret Fibonacci
while len(fib_sequence) < fib_limit:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)

# Mencetak jumlah bintang sesuai dengan angka Fibonacci
for num in fib_sequence:
    for _ in range(num):
        print("*", end=" ")
    print()