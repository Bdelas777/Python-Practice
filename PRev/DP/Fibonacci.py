def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]

def alt_fib(n, computed={0: 2, 1: 3}):
    if n in computed:
        return computed[n]
    computed[n] = alt_fib(n - 1, computed) + alt_fib(n - 2, computed)
    return computed[n]

# Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21
