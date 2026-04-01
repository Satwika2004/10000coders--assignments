--------- List-Based Interview Questions ---------

# 1. Add an Element to a List
# Manual
l = [1,2,3]
l += [4]
print(l)  # [1,2,3,4]
# Built-in
l = [1,2,3]
l.append(4)
print(l)  # [1,2,3,4]

# 2. Remove an Element from a List
# Manual
l = [1,2,3,4]
l = [x for x in l if x != 3]
print(l)  # [1,2,4]
# Built-in
l = [1,2,3,4]
l.remove(3)
print(l)  # [1,2,4]

# 3. Find Maximum in List
# Manual
l = [4,7,1,9]
max_val = l[0]
for x in l:
    if x > max_val:
        max_val = x
print(max_val)  # 9
# Built-in
print(max(l))  # 9

# 4. Find Minimum in List
# Manual
l = [4,7,1,9]
min_val = l[0]
for x in l:
    if x < min_val:
        min_val = x
print(min_val)  # 1
# Built-in
print(min(l))  # 1

# 5. Sum of All Elements in List
# Manual
l = [1,2,3]
sum_val = 0
for x in l:
    sum_val += x
print(sum_val)  # 6
# Built-in
print(sum(l))  # 6

# 6. Count Occurrence of an Element
# Manual
l = [1,2,2,3,2]
val = 2
count = 0
for x in l:
    if x == val:
        count += 1
print(count)  # 3
# Built-in
print(l.count(2))  # 3

# 7. Reverse a List
# Manual
l = [1,2,3]
rev = []
for i in range(len(l)-1,-1,-1):
    rev.append(l[i])
print(rev)  # [3,2,1]
# Built-in
l = [1,2,3]
l.reverse()
print(l)  # [3,2,1]

# 8. Sort a List
# Manual (Bubble Sort)
l = [4,1,3,2]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)  # [1,2,3,4]
# Built-in
print(sorted([4,1,3,2]))  # [1,2,3,4]

# 9. Remove Duplicates from a List
# Manual
l = [1,2,2,3]
res = []
for x in l:
    if x not in res:
        res.append(x)
print(res)  # [1,2,3]
# Built-in
print(list(set([1,2,2,3])))  # [1,2,3]

# 10. Merge Two Lists
# Manual
l1 = [1,2]; l2=[3,4]
merged = []
for x in l1:
    merged.append(x)
for x in l2:
    merged.append(x)
print(merged)  # [1,2,3,4]
# Built-in
print([1,2] + [3,4])  # [1,2,3,4]
# or
l1=[1,2]; l1.extend([3,4]); print(l1)  # [1,2,3,4]

# 11. Find Common Elements in Two Lists
# Manual
l1 = [1,2,3]; l2=[2,3,4]
common=[]
for x in l1:
    if x in l2:
        common.append(x)
print(common)  # [2,3]
# Built-in
print(list(set([1,2,3]) & set([2,3,4])))  # [2,3]

# 12. Print Even Numbers in a List
# Manual
l=[1,2,3,4]
evens=[]
for x in l:
    if x%2==0:
        evens.append(x)
print(evens)  # [2,4]


# 13. Print Odd Numbers in a List
# Manual
l=[1,2,3,4]
odds=[]
for x in l:
    if x%2!=0:
        odds.append(x)
print(odds)  # [1,3]
# Built-in
print([x for x in l if x%2!=0])  # [1,3]

# 14. Check if List is Palindrome
# Manual
l=[1,2,1]
is_palindrome = True
for i in range(len(l)//2):
    if l[i] != l[-i-1]:
        is_palindrome = False
print(is_palindrome)  # True
# Built-in
print(l == l[::-1])  # True

# 15. Count Positive, Negative, Zero
# Manual
l=[0,-1,2,-3,4]
pos=neg=zero=0
for x in l:
    if x>0: pos+=1
    elif x<0: neg+=1
    else: zero+=1
print("Positive:",pos,"Negative:",neg,"Zero:",zero)

# 16. Find Second Largest Number in List
# Manual
l=[1,3,4,5,0]
first=second=float('-inf')
for x in l:
    if x>first:
        second=first
        first=x
    elif x>second:
        second=x
print(second)  # 4
# Built-in
l_sorted = sorted(l, reverse=True)
print(l_sorted[1])  # 4

# 17. Find Second Smallest Number in List
# Manual
l=[5,1,4,2,3]
first=second=float('inf')
for x in l:
    if x<first:
        second=first
        first=x
    elif x<second:
        second=x
print(second)  # 2
# Built-in
print(sorted(l)[1])  # 2

# 18. Copy List to Another List
# Manual
l=[1,2,3]; copy=[]
for x in l:
    copy.append(x)
print(copy)  # [1,2,3]
# Built-in
copy = l.copy()
print(copy)  # [1,2,3]

# 19. Print All Prime Numbers in List
# Manual
def isprime(n):
    if n<2: return False
    for i in range(2,len(l)):
        if n%i==0: return False
    return True
l=[1,2,3,4,5]
primes=[]
for x in l:
    if isprime(x): primes.append(x)
print(primes)  # [2,3,5]


# 20. Replace All Zeroes with a Given Number
# Manual
l=[0,2,0,4]; rep=-1
for i in range(len(l)):
    if l[i]==0: l[i]=rep
print(l)  # [-1,2,-1,4]


# 21. Check if All Elements Are Same
# Manual
l=[5,5,5,5]
all_same=True
for i in range(1,len(l)):
    if l[i]!=l[0]: all_same=False
print(all_same)  # True
# Built-in
print(all(x==l[0] for x in l))  # True

# 22. Find Frequency of All Elements
# Manual
l=[1,2,2,3,1]; freq={}
for x in l:
    if x in freq: freq[x]+=1
    else: freq[x]=1
print(freq)  # {1:2,2:2,3:1}
# Built-in
from collections import Counter
print(dict(Counter(l)))  # {1:2,2:2,3:1}

# 23. Flatten a Nested List
# Manual
nested=[[1,2],[3,4]]; flat=[]
for sub in nested:
    for x in sub:
        flat.append(x)
print(flat)  # [1,2,3,4]


# 24. Split a List into Even and Odd Lists
# Manual
l=[1,2,3,4,5]; even=[]; odd=[]
for x in l:
    if x%2==0: even.append(x)
    else: odd.append(x)
print("Even:",even,"Odd:",odd)  # Even:[2,4] Odd:[1,3,5]


# 25. Find Pair of Elements with Given Sum
# Manual
l=[1,2,3,4]; target=5; pairs=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            pairs.append((l[i],l[j]))
print(pairs)  # [(1,4),(2,3)]


# 26. Remove All Odd Numbers
# Manual
l=[1,2,3,4,5]
res=[]
for x in l:
    if x%2==0: res.append(x)
print(res)  # [2,4]


# 27. Remove All Even Numbers
# Manual
l=[1,2,3,4,5]; res=[]
for x in l:
    if x%2!=0: res.append(x)
print(res)  # [1,3]


# 28. Multiply All Elements by a Number
# Manual
l=[1,2,3]; n=2; res=[]
for x in l: res.append(x*n)
print(res)  # [2,4,6]


# 29. Find Difference Between Max and Min
# Manual
l=[4,2,7,1]
max_val=l[0]; min_val=l[0]
for x in l:
    if x>max_val: max_val=x
    if x<min_val: min_val=x
print(max_val - min_val)  # 6
# Built-in
print(max(l)-min(l))  # 6

# 30. Check if a List is Empty
# Manual
l=[]
print(True if len(l)==0 else False)  # True
# Built-in
print(not l)  # True

# 31. Insert Element at Specific Index
# Built-in
l=[1,2,4]; l.insert(2,3)
print(l)  # [1,2,3,4]

# 32. Remove All Instances of a Value
# Manual
l=[1,2,2,3]; val=2
res=[]
for x in l:
    if x!=val: res.append(x)
print(res)  # [1,3]
# Built-in
l=[1,2,2,3]; val=2
while val in l: l.remove(val)
print(l)  # [1,3]

# 33. Get Index of an Element
# Built-in
print(l.index(20))  # 1

# 34. Square All Elements in a List
# Manual
l=[1,2,3]; res=[]
for x in l: res.append(x*x)
print(res)  # [1,4,9]


# 35. Filter Out Negative Numbers
# Manual
l=[-1,2,-3,4]; res=[]
for x in l:
    if x>=0: res.append(x)
print(res)  # [2,4]


# 36. Get Elements Greater Than a Value
# Manual
l=[1,5,8,3]; threshold=4; res=[]
for x in l:
    if x>threshold: res.append(x)
print(res)  # [5,8]


# 37. Find Duplicates in List
# Manual
l=[1,2,2,3,3,4]; res=[]
for x in l:
    if l.count(x)>1 and x not in res: res.append(x)
print(res)  # [2,3]


# 38. Rotate List Elements Right
# Manual
l=[1,2,3,4]; k=2
k=k%len(l)
l = l[-k:] + l[:-k]
print(l)  # [3,4,1,2]


# 39. Check If List Contains a Value
# Manual
l=[1,2,3]; val=2; found=False
for x in l:
    if x==val: found=True; break
print(found)  # True
# Built-in
print(val in l)  # True

# 40. Chunk List into Smaller Lists

# Built-in
import numpy as np
l=[1,2,3,4,5,6]
chunks = np.array_split(l,3)
print([list(x) for x in chunks])  # [[1,2],[3,4],[5,6]]
