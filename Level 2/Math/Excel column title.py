'''

Problem Description

Given a positive integer A, return its corresponding column title as appear in an Excel sheet.



Problem Constraints
1 <= A <= 1000000000



Input Format
First and only argument is integer A.



Output Format
Return a string, the answer to the problem.



Example Input
Input 1:

 A = 1
Input 2:

 A = 28


Example Output
Output 1:

 "A"
Output 2:

 "AB"


Example Explanation
Explanation 1:

 1 -> A
Explanation 2:

1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB

'''


class Solution:
    def convertToTitle(self, A):
        s = ""
        while A > 0:
            if A % 26 == 0:
                s += chr(26 + 64)
            else:
                s += chr(A % 26 + 64)
            A = (A - 1) // 26
        return s[::-1]


'''

class Solution:
    def convertToTitle(self, A):
        mydict = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        s = ''
        while A > 0:
            a = A%26
            s = mydict[a]+s
            A//=26
            if a == 0: A -= 1
        return s

'''
