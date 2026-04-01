# 1. Positive number (only if)
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")


# 2. Divisible by 5 (only if)
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")


# 3. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 4. Voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# 5. Grade system
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 6. Largest of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest is:", a)
elif b > c:
    print("Largest is:", b)
else:
    print("Largest is:", c)


# 7. Positive + Even/Odd (Nested)
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# 8. Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


# 9. Job eligibility
age = int(input("Enter age: "))
if age >= 21:
    qualification = input("Do you have degree (yes/no): ")
    if qualification == "yes":
        print("Eligible for job")
    else:
        print("Not eligible (no qualification)")
else:
    print("Not eligible (age)")


# ----------- Sample Input / Output -----------

# 1. Input: 5
# Output: Positive number

# 2. Input: 10
# Output: Divisible by 5

# 3. Input: 7
# Output: Odd number

# 4. Input: 16
# Output: Not eligible

# 5. Input: 82
# Output: Grade B

# 6. Input: 4, 7, 2
# Output: Largest is: 7

# 7. Input: 6
# Output:
# Positive number
# Even number

# 8. Input: admin, 1234
# Output: Login successful

# 9. Input: 22, yes
# Output: Eligible for job
