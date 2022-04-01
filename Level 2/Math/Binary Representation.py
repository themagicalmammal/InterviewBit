'''

Given a number N >= 0, find its representation in binary.

Example:

if N = 6,

binary form = 110

'''


class Solution:
    def findDigitsInBinary(self, A):
        if A == 0:
            return 0
        result = ''
        while A > 0:
            result += str(A % 2)
            A //= 2
        return result[::-1]


'''

class Solution:
    def findDigitsInBinary(self, A):
        if A == 0:
            return '0'
        result = ''
        while A > 0:
            result += str(A & 1)
            A >>= 1
        return result[::-1]

OR

class Solution:
    def findDigitsInBinary(self, A):
        return bin(A).replace("0b","")

'''
