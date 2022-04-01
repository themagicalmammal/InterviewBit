'''

Problem Description

Given a number A. Find the fatorial of the number.



Problem Constraints
1 <= A <= 100



Input Format
First and only argument is the integer A.



Output Format
Return a string, the factorial of A.



Example Input
Input 1:

A = 2
Input 2:

A = 3


Example Output
Output 1:

 2
Output 2:

 6


Example Explanation
Explanation 1:

2! = 2 .
Explanation 2:

3! = 6 .

'''


class Solution:
    def solve(self, A):
        s = 1
        for i in range(2, A + 1):
            s *= i
        return s


'''

class Solution:
    def solve(self, A):
        return(math.factorial(int(A)))

'''
