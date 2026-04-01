
# 1. Solid Square Pattern
n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

# 2. Solid Rectangle Pattern
rows = 3
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
# Input: rows=3, cols=5
# Output:
# * * * * *
# * * * * *
# * * * * *

# 3. Right-Angled Triangle (Left-Aligned)
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# 4. Right-Angled Triangle (Right-Aligned)
n = 5
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# 5. Inverted Triangle (Left-Aligned)
n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# 6. Inverted Triangle (Right-Aligned)
n = 5
for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# 7. Centered Pyramid Pattern
n = 4
for i in range(n):
    for j in range(n + i):
        if j < n-i-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *

# 8. Diamond Pattern
n = 3
for i in range(2*n-1):
    for j in range(2*n-1):
        if (i < n and j >= n-1-i and j <= n-1+i) or (i >= n and j >= i-(n-1) and j <= (3*n-3)-i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 3
# Output:
#   *
#  * * *
# * * * * *
#  * * *
#   *
# 9. Left-Aligned Half Diamond
n = 4
# Top part
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
# Bottom part
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# 10.Right-Aligned Half Diamond
n = 4
# Top part
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

# Bottom part
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
    
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *


# 11. Hollow Square Pattern
n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *

# 12. Hollow Rectangle Pattern
rows = 4
cols = 5
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: rows = 4, cols = 5
# Output:
# * * * * *
# *       *
# *       *
# * * * * *

# 13. Hollow Right-Angled Triangle (Left-Aligned)
n = 5
for i in range(n):
    for j in range(i+1):
        if i == n-1 or j == 0 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 5
# Output:
# *
# * *
# *   *
# *     *
# * * * * *

# 14. Hollow Right-Angled Triangle (Right-Aligned)
n = 5
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ", end=" ")
        elif i == n-1 or j == n-i-1 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 5
# Output:
#         *
#       * *
#     *   *
#   *     *
# * * * * *

# 15. Hollow Inverted Triangle (Left-Aligned)
n = 5
for i in range(n):
    for j in range(n-i):
        if i == 0 or j == 0 or j == n-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 5
# Output:
# * * * * *
# *     *
# *   *
# * *
# *

# 16. Hollow Inverted Triangle (Right-Aligned)
n = 5
for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end=" ")
        elif i == 0 or j == i or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 5
# Output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *

# 17. Hollow Pyramid Pattern
n = 4
for i in range(n):
    for j in range(n + i):
        if j < n-i-1:
            print(" ", end=" ")
        elif i == n-1 or j == n-i-1 or j == n+i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
#       *
#     *   *
#   *       *
# * * * * * * *

# 18. Hollow Diamond Pattern
n = 3
for i in range(2*n-1):
    for j in range(2*n-1):
        if (i < n and (j == n-1-i or j == n-1+i)) or (i >= n and (j == i-(n-1) or j == (3*n-3)-i)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 3
# Output:
#   *
#  * *
# *   *
#  * *
#   *

# 19. Hollow Butterfly Pattern
n = 4
for i in range(1, n+1):
    for j in range(1, 2*n+1):
        if j <= i or j > 2*n-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1, 2*n+1):
        if j <= i or j > 2*n-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *

# 20. Hollow Hourglass Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == i or j == n-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 5
# Output:
# * * * * *
#   *   *
#     *
#   *   *
# * * * * *

# 21. Increasing Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 22. Repeating Row Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()
# Input: n = 5
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# 23. Continuous Number Triangle
n = 4
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# 24. Reverse Row Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# 25. Inverted Number Triangle
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
# Input: n = 5
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# 26. Right-Aligned Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i:
            print(" ", end=" ")
        else:
            print(j-(n-i), end=" ")
    print()
# Input: n = 5
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# 27. Pyramid Number Pattern
n = 4
for i in range(1,n+1):
    for j in range(1,2*n):
        if j >= n-i+1 and j <= n+i-1:
            if j <= n:
                print(j-(n-i), end=" ")
            else:
                print(n-(j-n), end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

# 28. Even Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j, end=" ")
    print()
# Input: n = 5
# Output:
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

# 29. Odd Number Triangle
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(2*j+1, end=" ")
    print()
# Input: n = 5
# Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

# 30. Pascal’s Triangle
n = 5
for i in range(n):
    val = 1
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i-j) // (j+1)
    print()
# Input: n = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
