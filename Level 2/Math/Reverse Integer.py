'''

Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer

'''


class Solution:
    def reverse(self, A):
        A = str(A)[::-1]
        result = int('-' + A[:-1:] if A[-1] == '-' else A)
        return 0 if abs(result) > 2**31 - 1 else result


'''

class Solution:
    def reverse(self, A):
        sgn = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2**31 - 1:
            return 0
        return sgn * result

'''
