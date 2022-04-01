'''

The following code is supposed to rotate the array A by B positions.

So, for example,


A : [1 2 3 4 5 6]
B : 1

The output :

[2 3 4 5 6 1]
However, there is a small bug in the problem. Fix the bug and submit the problem.

 NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

'''


class Solution:
    def rotateArray(self, a, b):
        l = len(a)
        if b > l:
            b %= l
        return a[b:] + a[:b]


'''

class Solution:
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret

'''
