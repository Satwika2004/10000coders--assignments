# ================= 1. Solid Square Pattern =================
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

# ================= 2. Solid Rectangle Pattern =================
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

# ================= 3. Right-Angled Triangle (Left-Aligned) =================
n = 4
for i in range(1, n+1):
    print("* " * i)
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *

# ================= 4. Right-Angled Triangle (Right-Aligned) =================
n = 4
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *

# ================= 5. Inverted Triangle (Left-Aligned) =================
n = 4
for i in range(n, 0, -1):
    print("* " * i)
# Input: n = 4
# Output:
# * * * *
# * * *
# * *
# *

# ================= 6. Inverted Triangle (Right-Aligned) =================
n = 4
for i in range(n, 0, -1):
    print("  " * (n-i) + "* " * i)
# Input: n = 4
# Output:
# * * * *
#   * * *
#     * *
#       *

# ================= 7. Centered Pyramid Pattern =================
n = 4
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# Input: n = 4
# Output:
#    *
#   * *
#  * * *
# * * * *

# ================= 8. Diamond Pattern =================
n = 4
# Upper half
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# Lower half
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)
# Input: n = 4
# Output:
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

# ================= 9. Left-Aligned Half Diamond =================
n = 4
for i in range(1, n+1):
    print("* " * i)
for i in range(n-1, 0, -1):
    print("* " * i)
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

# ================= 10. Right-Aligned Half Diamond =================
n = 4
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print("  " * (n-i) + "* " * i)
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *

# ================= 11. Hollow Square Pattern =================
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

# ================= 12. Hollow Rectangle Pattern =================
rows = 3
cols = 5
for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: rows=3, cols=5
# Output:
# * * * * *
# *       *
# * * * * *

# ================= 13. Hollow Right-Angled Triangle (Left-Aligned) =================
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
# *
# * *
# *   *
# * * * *

# ================= 14. Hollow Right-Angled Triangle (Right-Aligned) =================
n = 4
for i in range(1, n+1):
    print("  " * (n-i), end="")
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
#       *
#     * *
#   *   *
# * * * *

# ================= 15. Hollow Inverted Triangle (Left-Aligned) =================
n = 4
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
# * * * *
# *   *
# * *
# *

# ================= 16. Hollow Inverted Triangle (Right-Aligned) =================
n = 4
for i in range(n, 0, -1):
    print("  " * (n-i), end="")
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Input: n = 4
# Output:
# * * * *
#   * *
#     *
#       *
