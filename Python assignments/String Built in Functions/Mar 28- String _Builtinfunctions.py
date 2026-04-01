# Date: 23-03-2026
# Tech stack : Python
# Topic: String Internal Functions

# 1. split()
def my_split(s):
    words = []
    temp = ""
    
    for ch in s:
        if ch != " ":
            temp += ch
        else:
            words.append(temp)
            temp = ""
    
    words.append(temp)
    return words

# Sample Input:
# s = "python is easy"
# Sample Output:
# ['python', 'is', 'easy']

print(my_split("python is easy"))

# 2. join()
def my_join(l):
    res = ""
    
    for i in range(len(l)):
        res += l[i]
        if i != len(l) - 1:
            res += " "
    
    return res

# Sample Input:
# l = ['python','is','easy']
# Sample Output:
# python is easy

print(my_join(['python','is','easy']))



# 3. center()
def my_center(s, width):
    total = width - len(s)
    left = total // 2
    right = total - left
    
    return " " * left + s + " " * right

# Sample Input:
# s = "hi", width = 6
# Sample Output:
# "  hi  "

print("'" + my_center("hi", 6) + "'")


# 4. zfill()
def my_zfill(s, width):
    if len(s) >= width:
        return s
    
    zeros = width - len(s)
    return "0" * zeros + s

# Sample Input:
# s = "45", width = 5
# Sample Output:
# 00045

print(my_zfill("45", 5))
