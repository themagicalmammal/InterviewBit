'''

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000
Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]

'''


class Solution:
    def generateMatrix(self, A):
        B = [[0] * A for _ in range(A)]
        L = T = 0
        R = C = A - 1
        d = 0
        j = 1
        while L <= R and T <= C:
            if d == 0:
                for i in range(L, R + 1):
                    B[T][i] = j
                    j += 1
                T += 1
            elif d == 1:
                for i in range(T, C + 1):
                    B[i][R] = j
                    j += 1
                R -= 1
            elif d == 2:
                for i in range(R, L - 1, -1):
                    B[C][i] = j
                    j += 1
                C -= 1
            elif d == 3:
                for i in range(C, T - 1, -1):
                    B[i][L] = j
                    j += 1
                L += 1
            d = (d + 1) % 4
        return B
