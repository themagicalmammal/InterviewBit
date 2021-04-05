'''

You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.

'''

class Solution:
    def subUnsort(self, A):
        b=sorted(A)
        L = [i for i in range(len(A)) if A[i]!=b[i]]
        if L:
            return [min(L),max(L)]
        return [-1]

'''

class Solution:
    def subUnsort(self, A):
        n = len(A)
        B = sorted(A)
        start = end = -1
        for i in range(n):
            A[i] -= B[i]
        for i in range(n):
            if A[i]!=0:
                if start==-1:
                    start=i
                end = max(i, end)
        if start==-1:
            return [-1]
        return [start, end]
        
'''