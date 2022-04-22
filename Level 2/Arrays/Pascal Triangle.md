'''

Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

'''


class Solution:
    def solve(self, A):
        B = [[1], [1, 1], [1, 2, 1]]
        l = len(B)
        if A > l:
            for i in range(l + 1, A + 1):
                z = []
                for j in range(i):
                    if j == 0 or j == i - 1:
                        z.append(1)
                    else:
                        z.append(B[-1][j] + B[-1][j - 1])
                B.append(z)
        return B[:A]


'''

class Solution:
    def solve(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1,r):
                row.append(result[r-1][i-1] + result[r-1][i])
            row.append(1)
            result.append(row)
        return result

OR

class Solution:
    def solve(self, A):
        P = []
        i = 0;
        while i < A:
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1);
                else:
                    row.append(P[i - 1][j-1] + P[i - 1][j])
            P.append(row)
            i += 1;
        return P

'''
