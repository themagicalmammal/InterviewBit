'''

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

'''


class Solution:
    def largestNumber(self, A):
        A = map(str, A)
        A.sort(lambda a, b: cmp(a + b, b + a), reverse=True)
        res = ''.join(A)
        return int(res)


'''

class Solution:
    def largestNumber(self,A):
        extval, ans = [], ""
        l = len(str(max(A))) + 1
        for i in A:
            temp = str(i) * l
            extval.append((temp[:l:], i))
        extval.sort(reverse = True)
        for i in extval:
            ans += str(i[1])
        return int(ans)

OR

from functools import cmp_to_key

class Solution:
	def largestNumber(self, A):
	    A = map(str, A)
	    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
	    res = ''.join(sorted(A, key= key, reverse=True))
	    res = res.lstrip('0')
	    return res if res else '0'

OR

class K:
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        return '%d%d'%(self.obj,other.obj) < '%d%d'%(other.obj,self.obj)

class Solution:
    def largestNumber(self, A):
        A = sorted(A, key=K, reverse=True)
        return str(int(''.join([str(s) for s in A])))
'''
