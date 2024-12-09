def print_fibonacci(length):
    # Handle the case for length 0 and 1
    if length == 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    
    # Starting the Fibonacci sequence with the first two numbers: 0 and 1
    fib_sequence = [0, 1]
    
    # Generate the sequence until it reaches the specified length
    for i in range(2, length):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
        fib_sequence.append(next_fib)  # Add the new number to the sequence
    
    # Print the Fibonacci sequence in the required format
    print(fib_sequence)

print_fibonacci(0)  
print_fibonacci(1)  
print_fibonacci(2)  
print_fibonacci(10) 