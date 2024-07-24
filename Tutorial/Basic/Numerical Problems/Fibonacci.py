def fibonacci(n):
    fib_sequence = [0, 1]
    
    if n <= 0:
        return 0
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Example usage
n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_sequence}")