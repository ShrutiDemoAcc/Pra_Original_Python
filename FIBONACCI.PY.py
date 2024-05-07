def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    for i in range(2, n):
        next_fib = fib_seq[-1] + fib_seq[-2]  # Calculate the next Fibonacci number
        fib_seq.append(next_fib)  # Add the next Fibonacci number to the sequence
    return fib_seq

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
fib_sequence = fibonacci(n)
print("Fibonacci Sequence of length", n, ":", fib_sequence)


