# List
numbers = [23, 76, 86, 7, 55, 33, 11, 76, 7]

# 1. Find the Largest Element
largest = max(numbers)
print("Largest element:", largest)

# 2. Remove Duplicates
unique_list = list(set(numbers))
print("List after removing duplicates:", unique_list)

# 3. Reverse a List (without using reverse())
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

# 4. Second Largest Number
sorted_list = sorted(set(numbers))
second_largest = sorted_list[-2]
print("Second largest element:", second_largest)

# 5. Count Even and Odd Numbers
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)


# ----------- Sample Input / Output -----------

# Sample List: [23, 76, 86, 7, 55, 33, 11, 76, 7]

# 1. Find the Largest Element
# Input: [23, 76, 86, 7, 55, 33, 11, 76, 7]
# Output: Largest element: 86

# 2. Remove Duplicates
# Input: [23, 76, 86, 7, 55, 33, 11, 76, 7]
# Output: List after removing duplicates: [33, 7, 76, 11, 86, 23, 55]

# 3. Reverse a List (without using reverse())
# Input: [23, 76, 86, 7, 55, 33, 11, 76, 7]
# Output: Reversed list: [7, 76, 11, 33, 55, 7, 86, 76, 23]

# 4. Second Largest Number
# Input: [23, 76, 86, 7, 55, 33, 11, 76, 7]
# Output: Second largest element: 76

# 5. Count Even and Odd Numbers
# Input: [23, 76, 86, 7, 55, 33, 11, 76, 7]
# Output: Even numbers count: 3
#         Odd numbers count: 6
