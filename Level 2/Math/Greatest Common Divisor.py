"""

Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 

"""


class Solution:
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)


"""

class Solution:
    def gcd(self, A, B):
        while B!=0:
            A, B= B, A%B
        return A

#Swap A, B if B > A
"""
