'''

You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : \[1 2 3 1 1\]
Output : 1
1 occurs 3 times which is more than 5/3 times.

'''

import random

class Solution:
def repeatedNumber(self, nums):
for i in range(20):
elem = random.choice(nums)
if nums.count(elem) > len(nums) // 3:
return elem
return -1

'''

import sys
def appearsNBy3(arr, n):
count1 = 0
count2 = 0
first = sys.maxsize
second = sys.maxsize
for i in range(0, n):
if (first == arr\[i\]):
count1 += 1
elif (second == arr\[i\]):
count2 += 1
elif (count1 == 0):
count1 += 1
first = arr\[i\]
elif (count2 == 0):
count2 += 1
second = arr\[i\]
else:
count1 -= 1
count2 -= 1
count1 = 0
count2 = 0
for i in range(0, n):
if (arr\[i\] == first):
count1 += 1

```
    elif (arr[i] == second):
        count2 += 1
if (count1 > n / 3):
    return first
if (count2 > n / 3):
    return second
return -1
```

'''
