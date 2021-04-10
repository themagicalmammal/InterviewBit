'''

Problem Description

Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.



**Problem Constraints**
1 <= A <= 10000



**Input Format**
First and only argumment is integer A.



**Output Format**
Return an integer, the answer to the problem.



**Example Input**
Input 1:

 A = 4
Input 2:

 A = 5


**Example Output**
Output 1:

 0
Output 2:

 1


**Example Explanation**
Explanation 1:

 4! = 24
Explanation 2:

 5! = 120

'''

class Solution:
    def trailingZeroes(self, A):
            if A//5 ==0:    
                return 0
            return (A//5)+self.trailingZeroes(A//5)

'''

class Solution:
    def trailingZeroes(self, A):
        c, i = 0, 5
        while A//i > 0:
            c += A // i
            i *= 5
        return c

'''