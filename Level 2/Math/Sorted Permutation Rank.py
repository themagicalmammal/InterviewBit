'''

Given a string, find the rank of the string amongst its permutations sorted lexicographically.

Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba

The answer might not fit in an integer, so return your answer % 1000003

'''


class Solution:
    def findRank(self, A):
        def fact(n):
            if n == 0:
                return 1
            return (n * fact(n - 1)) % mod
        mod = 1000003
        ans = 0
        n = len(A)
        for i in range(n - 1):
            c = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    c += 1
            ans += (c * fact(n - i - 1))
        return(ans + 1) % mod
