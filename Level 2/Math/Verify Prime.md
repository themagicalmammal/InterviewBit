'''

Given a number N, verify if N is prime or not.

Return 1 if N is prime, else return 0.

Example :

Input : 7
Output : True

'''


class Solution:
    def isPrime(self, p):
        if p == 1 or p % 2 == 0:
            return 0
        for i in range(3, int(p**0.5) + 1, 2):
            if p % i == 0:
                return 0
        return 1
