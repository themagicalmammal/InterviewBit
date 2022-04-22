'''

A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
OR  : (0, 0) -> (1, 0) -> (1, 1)

'''

from math import factorial as f

class Solution:
def uniquePaths(self, A, B):
return f(A + B - 2) // f(A - 1) // f(B - 1)

'''

class Solution:
def uniquePaths(self, A, B):
numPaths = \[\[1 for _ in range(B)\] for _ in range(A)\]
for i in range(1,A):
for j in range(1,B):
numPaths\[i\]\[j\] = numPaths\[i-1\]\[j\] + numPaths\[i\]\[j-1\]
return numPaths\[-1\]\[-1\]

'''
