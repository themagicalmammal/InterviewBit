'''

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:


Input:

1 2 3
4 5 6
7 8 9

Return the following :

[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input :
1 2
3 4

Return the following  :

[
  [1],
  [2, 3],
  [4]
]

'''


class Solution:
    def diagonal(self, A):
        a = len(A)
        B = [[] for i in range(a * 2 - 1)]
        for i in range(a):
            for j in range(a):
                B[i + j].append(A[i][j])
        return B
