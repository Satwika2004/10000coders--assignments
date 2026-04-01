
# March 7 Assignment - List Slicing Practice

l = [11, 22, 33, 44, 55, 66, 7, 88, 86, 78, 76, 10, 23]

# 1. Reverse every second element
print(l[::-2])  # output:[23, 76, 86, 7, 55, 33, 11]

# 2. From -5 index to start, reversed
print(l[-5::-1]) # output:[86, 88, 7, 66, 55, 44, 33, 22, 11]

# 3. Full reversed list
print(l[::-1]) # output: [23, 10, 76, 78, 86, 88, 7, 66, 55, 44, 33, 22, 11]

# 4. Every second element from start to end
print(l[0:len(l):2])  # output: [11, 33, 55, 7, 86, 76, 23]

# 5. Every second element (shorthand)
print(l[::2]) # output: [11, 33, 55, 7, 86, 76, 23]

# 6. Sublist from index 2 to 6
print(l[2:7]) # output: [33, 44, 55, 66, 7] 

# 7. First 4 elements
print(l[:4]) # output: [11, 22, 33, 44]

# 8. From index 2 to end
print(l[2:]) # output: [33, 44, 55, 66, 7, 88, 86, 78, 76, 10, 23]

# 9. From index 1 to 5
print(l[1:6]) 3 output: [22, 33, 44, 55, 66]

# 10. First 6 elements
print(l[:6]) # output: [11, 22, 33, 44, 55, 66]

# 11. From index 7 to end (with step 1)
print(l[7:len(l):1]) # output: [88, 86, 78, 76, 10, 23]

# 12. Shorthand from index 7 to end
print(l[7:len(l)]) # output: [88, 86, 78, 76, 10, 23] 

# 13. From index 7 to end (even shorter)
print(l[7:]) # output: [88, 86, 78, 76, 10, 23]

# 14. First 6 elements (with step 1)
print(l[0:6:1]) # output:[11, 22, 33, 44, 55, 66]

# 15. First 6 elements (shorthand)
print(l[0:6]) # output:[11, 22, 33, 44, 55, 66]

# 16. First 6 elements (even shorter)
print(l[:6]) # output:[11, 22, 33, 44, 55, 66]
