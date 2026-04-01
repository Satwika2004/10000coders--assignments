# 5. Internal implementation of String method  isupper()
def isupper_manual(s):
    for ch in s:
        if ch.isalpha() and not ('A' <= ch <= 'Z'):
            return False
    return True

# Sample Input
s = "HELLO"
print(isupper_manual(s))  # Output: True

s2 = "Hello"
print(isupper_manual(s2)) # Output: False

#6. Internal implementation of String method startswith()
def startswith_manual(s, sub):
    if s[:len(sub)] == sub:
        return True
    return False

# Sample Input
s = "Python Programming"
print(startswith_manual(s, "Python"))  # Output: True
print(startswith_manual(s, "Java"))    # Output: False

#7. Internal implementation of String method endswith()
def endswith_manual(s, sub):
    if s[-len(sub):] == sub:
        return True
    return False

# Sample Input
s = "Python Programming"
print(endswith_manual(s, "ming"))  # Output: True
print(endswith_manual(s, "Python"))# Output: False


8. Internal implementation of String method istitle()
def istitle_manual(s):
    words = s.split()
    for word in words:
        if len(word) > 0:
            if not ('A' <= word[0] <= 'Z'):
                return False
            for ch in word[1:]:
                if 'A' <= ch <= 'Z':
                    return False
    return True

# Sample Input
s = "Python Programming"
print(istitle_manual(s))  # Output: True

s2 = "Python programming"
print(istitle_manual(s2)) # Output: False
