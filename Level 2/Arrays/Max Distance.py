'''

Problem Description

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].



Input Format
First and only argument is an integer array A.



Output Format
Return an integer denoting the maximum value of j - i;



Example Input
Input 1:

 A = [3, 5, 4, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Maximum value occurs for pair (3, 4).

'''


class Solution:
    def maximumGap(self, A):
        B = list(range(len(A)))
        B.sort(key=lambda i: A[i])
        m = 0
        s = B[0]
        for i in B:
            if i <= s:
                s = i
            else:
                m = max(m, i - s)
        return m


'''

class Solution:
    def maximumGap(self, A):
        A = list(A)
        B = {}
        for i in range(len(A)):
            if A[i] in B:
                B[A[i]].append(i)
            else:
                B[A[i]] = [i]
        A.sort(reverse  = False)
        diff = 0
        temp = len(A)
        for i in range(len(A)):
            if temp > B[A[i]][0]:
                temp = B[A[i]][0]
            diff = max(diff, B[A[i]][-1] - temp)
        return diff

'''
