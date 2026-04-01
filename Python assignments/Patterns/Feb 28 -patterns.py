# 1. Nearest Prime
num = int(input("Enter number: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

i = num
while True:
    if is_prime(i):
        print("Nearest prime:", i)
        break
    i += 1


# 2. Square Pattern
n = int(input("Enter size: "))
for i in range(1,n+1):
    for j in range1,n+1):
        print("*", end=" ")
    print()

# Hollow Square
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Rectangle
r = int(input("Rows: "))
c = int(input("Cols: "))

for i in range(1,r+1):
    for j in range(1,c+1):
        print("*", end=" ")
    print()

# Hollow Rectangle
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or j==1 or j==c:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 4. Right Triangle (Left)
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Right Triangle (Right)
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# 5. Inverse Triangle (Left)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Inverse Triangle (Right)
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()




# 1. Nearest Prime
# Input: 20
# Output: Nearest prime: 19

# 2. Square Pattern
# Input: 4
# Output:
* * * * 
* * * * 
* * * * 
* * * * 

# Hollow Square
* * * *
*     *
*     *
* * * *

# 3. Rectangle
# Input: rows=3, cols=5
# Output:
* * * * * 
* * * * * 
* * * * * 

# Hollow Rectangle
* * * * *
*       *
* * * * *

# 4. Right Angled Triangle
# Input: size=4
# Left Aligned
* 
* * 
* * * 
* * * * 

# Right Aligned
      * 
    * * 
  * * * 
* * * * 

# 5. Inverse Right Angled Triangle
# Left Inverse
* * * * 
* * * 
* * 
* 

# Right Inverse
* * * * 
  * * * 
    * * 
      *
