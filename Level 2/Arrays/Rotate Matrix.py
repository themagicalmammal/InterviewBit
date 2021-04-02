'''

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]

'''

class Solution:
    def rotate(self, A):
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        N = len(A)
        for i in range(N/2):
            for j in range(N):
             A[j][i], A[j][N-1-i] = A[j][N-1-i],A[j][i]
        return (A)

'''

class Solution:
    def rotate(self, A):
        N = len(A)
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
                A[j][N - 1 - i] = temp
        return A

'''