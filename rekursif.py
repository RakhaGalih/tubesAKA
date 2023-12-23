def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Try running with n = 10
result_recursive = fibonacci_recursive(10)
print("Result (n=100) using recursive:", result_recursive)