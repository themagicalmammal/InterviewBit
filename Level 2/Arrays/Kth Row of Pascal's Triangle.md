'''

Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?

'''


class Solution:
    def getRow(self, A):
        B = [[1], [1, 1], [1, 2, 1]]
        l = len(B)
        if A + 1 > l:
            for i in range(l + 1, A + 2):
                z = []
                for j in range(i):
                    if j == 0 or j == i - 1:
                        z.append(1)
                    else:
                        z.append(B[-1][j] + B[-1][j - 1])
                B.append(z)
        return B[A]


'''

class Solution:
    def getRow(self, A):
        curr = [1]*(A+1)
        if A<2 : return curr
        prev = self.getRow(A-1)
        for i in range(1,A):
            curr[i] = prev[i]+prev[i-1]
        return curr

'''
