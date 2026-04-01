# 1. Print 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i, end=" ")
print()

# 2. m to n
m = int(input("Enter m: "))
n = int(input("Enter n: "))
for i in range(m, n+1):
    print(i, end=" ")
print()

# 3. n to 1
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(i, end=" ")
print()

# 4. n to m reverse
n = int(input("Enter n: "))
m = int(input("Enter m: "))
for i in range(n, m-1, -1):
    print(i, end=" ")
print()

# 5. Sum of n
n = int(input("Enter n: "))
s = 0
for i in range(1, n+1):
    s += i
print(s)

# 6. Factorial
n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 7. Sum m to n
m = int(input("Enter m: "))
n = int(input("Enter n: "))
s = 0
for i in range(m, n+1):
    s += i
print(s)

# 8. Product m to n
m = int(input("Enter m: "))
n = int(input("Enter n: "))
p = 1
for i in range(m, n+1):
    p *= i
print(p)

# 9. Factors
n = int(input("Enter n: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()

# 10. Count factors
n = int(input("Enter n: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)

# 11. Prime
n = int(input("Enter n: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

# 12. Even m to n
m = int(input())
n = int(input())
for i in range(m, n+1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 13. Odd m to n
m = int(input())
n = int(input())
for i in range(m, n+1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# 14. Count even/odd
m = int(input())
n = int(input())
even = odd = 0
for i in range(m, n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even, "Odd =", odd)

# 15. Reverse string
s = input()
print(s[::-1])

# 16. Palindrome string
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 17. Sum of digits
n = int(input())
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)

# 18. Product of digits
n = int(input())
p = 1
while n > 0:
    p *= n % 10
    n //= 10
print(p)

# 19. Armstrong
n = int(input())
temp = n
s = 0
while n > 0:
    d = n % 10
    s += d**3
    n //= 10
if s == temp:
    print("Armstrong number")
else:
    print("Not Armstrong")

# 20. Reverse number
n = int(input())
rev = 0
while n > 0:
    rev = rev*10 + n % 10
    n //= 10
print(rev)

# 21. Palindrome number
n = int(input())
temp = n
rev = 0
while n > 0:
    rev = rev*10 + n % 10
    n //= 10
if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")

# 22. Count vowels
s = input()
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)

# 23. Count consonants
s = input()
count = 0
for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count += 1
print(count)

# 24. Vowels & consonants
s = input()
v = c = 0
for ch in s:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch.isalpha():
        c += 1
print("Vowels =", v, "Consonants =", c)

# 25. Perfect number
n = int(input())
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print("Perfect number")
else:
    print("Not Perfect")

# 26. Neon number
n = int(input())
sq = n*n
s = 0
while sq > 0:
    s += sq % 10
    sq //= 10
if s == n:
    print("Neon number")
else:
    print("Not Neon")

# 27. Strong number
n = int(input())
temp = n
s = 0
while n > 0:
    d = n % 10
    f = 1
    for i in range(1, d+1):
        f *= i
    s += f
    n //= 10
if s == temp:
    print("Strong number")
else:
    print("Not Strong")

# 28. Harshad number
n = int(input())
temp = n
s = 0
while n > 0:
    s += n % 10
    n //= 10
if temp % s == 0:
    print("Harshad number")
else:
    print("Not Harshad")

# 29. Fibonacci
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b






# ----------- Sample Input / Output -----------

# 1. Input: 5
# Output: 1 2 3 4 5

# 2. Input: 3, 7
# Output: 3 4 5 6 7

# 3. Input: 5
# Output: 5 4 3 2 1

# 4. Input: 10, 6
# Output: 10 9 8 7 6

# 5. Input: 5
# Output: 15

# 6. Input: 5
# Output: 120

# 7. Input: 3, 6
# Output: 18

# 8. Input: 2, 4
# Output: 24

# 9. Input: 6
# Output: 1 2 3 6

# 10. Input: 6
# Output: 4

# 11. Input: 7
# Output: Prime

# 12. Input: 3, 10
# Output: 4 6 8 10

# 13. Input: 3, 10
# Output: 3 5 7 9

# 14. Input: 3, 7
# Output: Even = 2, Odd = 3

# 15. Input: hello
# Output: olleh

# 16. Input: madam
# Output: Palindrome

# 17. Input: 123
# Output: 6

# 18. Input: 123
# Output: 6

# 19. Input: 153
# Output: Armstrong number

# 20. Input: 123
# Output: 321

# 21. Input: 121
# Output: Palindrome

# 22. Input: apple
# Output: 2

# 23. Input: apple
# Output: 3

# 24. Input: apple
# Output: Vowels = 2, Consonants = 3

# 25. Input: 28
# Output: Perfect number

# 26. Input: 9
# Output: Neon number

# 27. Input: 145
# Output: Strong number

# 28. Input: 18
# Output: Harshad number

# 29. Input: 5
# Output: 0 1 1 2 3
