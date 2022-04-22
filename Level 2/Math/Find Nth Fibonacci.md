'''

Problem Description

Given an integer A you need to find the Ath fibonacci number modulo 109 + 7.

The first fibonacci number F1 = 1

The first fibonacci number F2 = 1

The nth fibonacci number Fn = Fn-1 + Fn-2 (n > 2)



Problem Constraints

1 <= A <= 109.


Input Format

First argument is an integer A.


Output Format

Return a single integer denoting Ath fibonacci number modulo 109 + 7.


Example Input

Input 1:

 A = 4

Input 2:

 A = 3



Example Output

Output 1:

 3

Output 2:

 2



Example Explanation

Explanation 1:

 F3 = F2 + F1 = 1 + 1 = 2
 F4 = F3 + F2 = 2 + 1 = 3

Explanation 2:

 F3 = F2 + F1 = 1 + 1 = 2

'''


class Solution:
    def fibi(self, n, d={}):
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        elif n == 4:
            return 3
        if n in d:
            return d[n]
        elif n % 2 != 0:
            d[n] = (self.fibi(n // 2)**2 +
                    self.fibi(n // 2 + 1)**2) % (10**9 + 7)
            return d[n]
        else:
            d[n] = (2 * self.fibi(n // 2)**2 + self.fibi(n // 2 - 3)
                    * self.fibi(n // 2)) % (10**9 + 7)
            return d[n]

    def solve(self, a):
        return self.fibi(a)

 '''
 
from numpy import matrix, array
class Solution:
    def solve(self, A):
        by = 10**9+7
        if A in [1,2]:
            return 1
        M = matrix([[1,1],[1,0]],dtype=int)
        def ret(N):
            if N == 1 :
                return M
            M1 = ret(N//2)
            return (M1*M1*M)%by if N%2 else (M1*M1)%by
        return array(ret(A-1)*M)[0][0]
        
 '''
