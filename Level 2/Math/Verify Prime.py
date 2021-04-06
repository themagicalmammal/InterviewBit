'''

Given a number N, verify if N is prime or not.

Return 1 if N is prime, else return 0.

Example :

Input : 7
Output : True

'''

from math import sqrt
class Solution:
    def isPrime(self, p):
        if p < 2: return 0
        for i in range(2,int(sqrt(p))+1):
            if p % i == 0:
                return 0
        return 1