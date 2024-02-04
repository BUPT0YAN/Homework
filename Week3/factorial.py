"""
Factorial Calculator Function

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number):
    # Your code goes here
    # Implement the factorial calculation using a for loop
    num = int(input("Please enter"))
    fac = 1
    if num == 0:
        return 1
    if num > 0:
        for i in range(num):
            fac = fac*(i+1)
            i = i + 1 #i从0开始所以i+1最大到输入数字
        return fac
    else:
        return "Error message or specific value"
    pass  # Delete this after implementing some code inside this function


# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
