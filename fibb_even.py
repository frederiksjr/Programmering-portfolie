def fibonacci(max_n):
    n, prev = 1, 1
    while n <= max_n:
        yield n
        n, prev = n + prev, n

total = sum(n for n in fibonacci(4000000) if n % 2 == 0)
print(total)