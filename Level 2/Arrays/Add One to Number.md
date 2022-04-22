'''

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

'''


class Solution:
    def plusOne(self, A):
        for i in range(len(A) - 1, -1, -1):
            A[i] += 1
            if A[i] > 9:
                z = str(A[i])
                A[i] = int(z[-1])
                if i == 0:
                    A.insert(0, 1)
            else:
                break
        while A[0] == 0:
            A.pop(0)
        return A


'''

class Solution:
    def plusOne(self, A):
        for i in range(len(A)-1, -1, -1):
            if A[i] == 9:
                A[i] = 0
            else:
                A[i] += 1
                while A[0] == 0:
                    del A[0]
                return A
        return [1] + A

'''
