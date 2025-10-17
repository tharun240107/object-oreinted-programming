import time

# ------------------ FACTORIAL ------------------

# Recursive factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ------------------ FIBONACCI ------------------

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ------------------ MAIN PROGRAM ------------------

n = int(input("Enter a number: "))

# ----- Factorial -----
start = time.time()
fact_r = factorial_recursive(n)
end = time.time()
print(f"Recursive Factorial of {n} = {fact_r}")
print(f"Time (recursive): {end - start:.8f} seconds")

start = time.time()
fact_i = factorial_iterative(n)
end = time.time()
print(f"Iterative Factorial of {n} = {fact_i}")
print(f"Time (iterative): {end - start:.8f} seconds")

print("-" * 50)

# ----- Fibonacci -----
start = time.time()
fib_r = fibonacci_recursive(n)
end = time.time()
print(f"Recursive Fibonacci({n}) = {fib_r}")
print(f"Time (recursive): {end - start:.8f} seconds")

start = time.time()
fib_i = fibonacci_iterative(n)
end = time.time()
print(f"Iterative Fibonacci({n}) = {fib_i}")
print(f"Time (iterative): {end - start:.8f} seconds")
