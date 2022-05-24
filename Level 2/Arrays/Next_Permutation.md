'''

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

Note:

1. The replacement must be in-place, do **not** allocate extra memory.
1. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
   Input Format:

The first and the only argument of input has an array of integers, A.
Output Format:

Return an array of integers, representing the next permutation of the given array.
Constraints:

1 \<= N \<= 5e5
1 \<= A\[i\] \<= 1e9
Examples:

Input 1:
A = \[1, 2, 3\]

Output 1:
\[1, 3, 2\]

Input 2:
A = \[3, 2, 1\]

Output 2:
\[1, 2, 3\]

Input 3:
A = \[1, 1, 5\]

Output 3:
\[1, 5, 1\]

Input 4:
A = \[20, 50, 113\]

Output 4:
\[20, 113, 50\]

'''

class Solution:
def nextPermutation(self, A):
n = len(A)
ind = -1
for i in range(n - 2, -1, -1):
if A\[i\] \< A\[i + 1\]:
ind = i
if ind == -1:
return A\[::-1\]
for j in range(n - 1, ind, -1):
if A\[j\] > A\[ind\]:
A\[ind\], A\[j\] = A\[j\], A\[ind\]
break
return A\[:ind + 1\] + A\[n:ind:-1\]

'''

class Solution:
def nextPermutation(self,A):

```
    i = -1
    j = len(A)-1

    for k in reversed(range(len(A))):
        if A[k]>A[k-1]:
            i=k-1
            break

    for k in range(len(A)-1,0,-1):
        if A[k]>A[i]:
            j=k
            break

    A[i],A[j]=A[j],A[i]

    left = i+1
    right = len(A)-1

    while(left<right):
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1

    return A
```

'''
