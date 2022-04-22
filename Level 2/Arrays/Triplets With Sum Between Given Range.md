'''

Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.

Example:

Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

You should return 1

as

0.6+0.7+0.4=1.7

1<1.7<2

Hence, the output is 1.

O(n) solution is expected.

Note: You can assume the numbers in strings don’t overflow the primitive data type and there are no leading zeroes in numbers. Extra memory usage is allowed.

'''


class Solution:
    def solve(self, A):
        a, b, c = float(A[0]), float(A[1]), float(A[2])
        for i in range(3, len(A)):
            if 2 > a + b + c > 1:
                return 1
            elif a + b + c > 2:
                x = max(a, b, c)
                if a == x:
                    a = float(A[i])
                elif b == x:
                    b = float(A[i])
                else:
                    c = float(A[i])
            else:
                x = min(a, b, c)
                if x == a:
                    a = float(A[i])
                elif x == b:
                    b = float(A[i])
                else:
                    c = float(A[i])
        if 2 > a + b + c > 1:
            return 1
        return 0
