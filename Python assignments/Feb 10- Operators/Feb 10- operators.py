# Feb 10 - Operators Assignment

# 1. Swap two numbers without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swapping: a = {a} and b = {b}")
a, b = b, a
print(f"After swapping: a = {a} and b = {b}")


# 2. Check positive, negative or zero
num = int(input("Enter a number: "))
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")


# 3. Area of rectangle and check square
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = length * breadth
print(f"Area of rectangle is : {area}")
if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")


# 4. Simple Interest
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
print(f"Simple Interest is: {SI}")


# 5. Bitwise operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# ----------- Sample Input / Output -----------

# 1. Swap
# Input:
# Enter first number: 3
# Enter second number: 4
# Output:
# Before swapping: a = 3 and b = 4
# After swapping: a = 4 and b = 4

# 2. Positive/Negative
# Input:
# Enter a number: -5
# Output:
# Negative

# 3. Rectangle
# Input:
# Enter length: 5
# Enter breadth: 5
# Output:
# Area of rectangle is : 25
# It is a Square

# 4. Simple Interest
# Input:
# Enter Principal: 1000
# Enter Rate: 5
# Enter Time: 2
# Output:
# Simple Interest is: 100.0

# 5. Bitwise
# Input:
# Enter first number: 5
# Enter second number: 3
# Output:
# AND: 1
# OR: 7
# XOR: 6
# Left Shift: 10
# Right Shift: 2
