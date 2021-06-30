'''

Problem Description

Given a number A in a form of string.

You have to find the smallest number that has same set of digits as A and is greater than A.

If A is the greatest possible number with its set of digits, then return -1.



Problem Constraints

 1 <= A <= 10100000

 A doesn't contain leading zeroes.



Input Format

First and only argument is an numeric string denoting the number A.


Output Format

Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.


Example Input

Input 1:

 A = "218765"

Input 2:

 A = "4321"



Example Output

Output 1:

 "251678"

Output 2:

 "-1"



Example Explanation

Explanation 1:

 The smallest number greater then 218765 with same set of digits is 251678.

Explanation 2:

 The given number is the largest possible number with given set of digits so we will return -1.
 
'''

class Solution:
    def solve(self, s):
        for i in range(len(s) - 2, -1, -1):
            tail = sorted(s[i:])
            for j in range(len(tail)):
                m = int(s[:i] + tail[j] + ''.join(tail[:j] + tail[j+1:]))
                if m > int(s):
                    return m
        return '-1'
        
'''

class Solution:
    def solve(self, A):
        l=len(A)
        idx=l-2
        while idx>=0:
            if A[idx]<A[idx+1]:
                j=l-1
                while A[j]<=A[idx]:
                    j-=1
                A=A[:idx]+A[j]+A[l-1:j:-1]+A[idx]+A[j-1:idx:-1]
                return(A)
            idx-=1
        return('-1')
        
'''
