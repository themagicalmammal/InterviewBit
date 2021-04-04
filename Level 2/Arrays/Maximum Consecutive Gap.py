'''

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5 
Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.

'''

class Solution:
    def maximumGap(self, A):
        A=sorted(A)
        m=0
        for j in range(len(A)-1):
            m=max(m, A[j+1]-A[j])
        return m