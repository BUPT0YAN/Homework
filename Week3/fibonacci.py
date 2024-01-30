"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):
    # Your code goes here
    # Implement the Fibonacci sequence calculation using a while loop
    #fib = [0]
    
    fib1 = 0
    fib2 = 1 
    fib = [fib1,fib2]
    sum = 0
    num = int(input("Please enter"))
    if num == 0:
        fib = [0]
        return fib
    elif num > 0:
        while sum <= num:
            sum = fib1 + fib2
            if sum > num:
                break
            else:
                fib.append(sum)
                fib1 = fib2
                fib2 = sum
        return fib        
    else:
        return "Empty list or error message"
    pass  # Delete this after implementing some code inside this function


# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
