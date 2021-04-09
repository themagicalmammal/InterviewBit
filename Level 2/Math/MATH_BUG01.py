'''

Following code tries to figure out if a number is prime ( Wiki )
However, it has a bug in it.
Please correct the bug and then submit the code.

'''

class Solution:
    def isPrime(self, A):
        if A ==1: return 0
        for i in xrange(2, int(A**0.5) + 1):
            if A % i == 0:
                return 0
        return 1