# Assignment - Conditional Problems

# 1. Even or Odd
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2. Divisible by 5 but not 10
n = int(input("Enter number: "))
if n % 5 == 0 and n % 10 != 0:
    print("Satisfy")
else:
    print("Not satisfy")


# 3. Biggest among two numbers
a = int(input("Enter A: "))
b = int(input("Enter B: "))
if a > b:
    print("Biggest is:", a)
else:
    print("Biggest is:", b)


# 4. Smallest among two numbers
a = int(input("Enter A: "))
b = int(input("Enter B: "))
if a < b:
    print("Smallest is:", a)
else:
    print("Smallest is:", b)


# 5. Divisible by 2, 3 and 6
n = int(input("Enter number: "))
if n % 2 == 0 and n % 3 == 0:
    print("Satisfy")
else:
    print("Not satisfy")


# 6. Voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# 7. Pass/Fail (all subjects)
m = int(input("Maths: "))
p = int(input("Physics: "))
c = int(input("Chemistry: "))
if m >= 35 and p >= 35 and c >= 35:
    print("Pass")
else:
    print("Fail")


# 8. Pass if any one subject
if m >= 35 or p >= 35 or c >= 35:
    print("Pass")
else:
    print("Fail")


# 9. Pass if any two subjects
count = 0
if m >= 35:
    count += 1
if p >= 35:
    count += 1
if c >= 35:
    count += 1

if count >= 2:
    print("Pass")
else:
    print("Fail")


# 10. Biggest among three
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
if a > b and a > c:
    print("Biggest is:", a)
elif b > c:
    print("Biggest is:", b)
else:
    print("Biggest is:", c)


# 11. Smallest among three
if a < b and a < c:
    print("Smallest is:", a)
elif b < c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)


# 12. Perfect square
n = int(input("Enter number: "))
root=int(n**0.5)
if root*root=n:
    print("Perfect square")
else:
    print("Not perfect square")


# 13. Cars required
members = int(input("Enter members: "))
if members%5==0:
  print("cars needed=", members//5)
else:
  print("cars needed=", members//5+1)



# 14. Second biggest among three
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if (a > b and a < c) or (a > c and a < b):
    print("Second biggest:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Second biggest:", b)
else:
    print("Second biggest:", c)


# 15. Leap year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")




# ----------- Sample Input / Output -----------

# 1. Input: 6
# Output: Even number

# 2. Input: 25
# Output: Satisfy

# 3. Input: 4, 7
# Output: Biggest is: 7

# 4. Input: 4, 7
# Output: Smallest is: 4

# 5. Input: 18
# Output: Satisfy

# 6. Input: 19
# Output: Eligible to vote

# 7. Input: 40, 36, 30
# Output: Fail

# 8. Input: 20, 38, 25
# Output: Pass

# 9. Input: 40, 20, 36
# Output: Pass

# 10. Input: 7, 4, 9
# Output: Biggest is: 9

# 11. Input: 7, 4, 9
# Output: Smallest is: 4

# 12. Input: 49
# Output: Perfect square

# 13. Input: 17
# Output: Cars needed = 4

# 14. Input: 10, 25, 18
# Output: Second biggest: 18

# 15. Input: 2024
# Output: Leap year
