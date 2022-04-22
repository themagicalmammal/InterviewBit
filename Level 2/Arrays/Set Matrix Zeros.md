'''

Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.
Constraints:

1 \<= N, M \<= 1000
0 \<= A\[i\]\[j\] \<= 1
Examples:

Input 1:
\[   \[1, 0, 1\],
\[1, 1, 1\],
\[1, 1, 1\]   \]

Output 1:
\[   \[0, 0, 0\],
\[1, 0, 1\],
\[1, 0, 1\]   \]

Input 2:
\[   \[1, 0, 1\],
\[1, 1, 1\],
\[1, 0, 1\]   \]

Output 2:
\[   \[0, 0, 0\],
\[1, 0, 1\],
\[0, 0, 0\]   \]

'''

class Solution:
def setZeroes(self, A):
rows = set()
cols = set()
for i in range(len(A)):
for j in range(len(A\[0\])):
if A\[i\]\[j\] == 0:
rows.add(i)
cols.add(j)
for i in rows:
for j in range(len(A\[0\])):
A\[i\]\[j\] = 0
for j in cols:
for i in range(len(A)):
A\[i\]\[j\] = 0
return A

'''

class Solution:
def setZeroes(self, A):
N = len(A)
M = len(A\[0\])
del_first_row = False
del_first_col = False

```
    for i in xrange(N):
        if A[i][0] == 0:
            del_first_row = True
            break
    for i in xrange(M):
        if A[0][i] == 0:
            del_first_col = True
            break

    for i in xrange(N):
        for j in xrange(M):
            if A[i][j] == 0:
                A[i][0] = 2
                A[0][j] = 2


    for i in xrange(1,N):
        for j in xrange(1,M):
            if A[i][0] == 2:
                A[i][j] = 0
            elif A[0][j] == 2:
                A[i][j] = 0
    for i in xrange(N):
        if A[i][0] > 1 or del_first_row:
            A[i][0] = 0
    for i in xrange(M):
        if A[0][i] > 1 or del_first_col:
            A[0][i] = 0

    return A
```

'''
