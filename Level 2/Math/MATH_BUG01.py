'''

Following code tries to figure out if a number is prime ( Wiki )
However, it has a bug in it.
Please correct the bug and then submit the code.

'''

class Solution:
    def isPrime(self, A):
        if A ==1:
           return 0
        elif A < 3:
           return 1
        upperLimit = int(A**0.5)
        for i in xrange(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1