# Function 1: Add
def add(a, b):
    return a + b

# Function 2: Multiply
def multiply(a, b):
    return a * b

# Function 3: Is Even
def is_even(n):
    return n % 2 == 0

# Function 4: Reverse String
def reverse_string(s):
    return s[::-1]

# Function 5: Find Max
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Testing all functions
print(add(5, 3))
print(multiply(4, 6))
print(is_even(10))
print(reverse_string("Sheshandra"))
print(find_max([3, 7, 1, 9, 4]))