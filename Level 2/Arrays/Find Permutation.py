'''

Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :

Input 1:

n = 3

s = ID

Return: [1, 3, 2]

'''

class Solution:
    def findPerm(self, s, n):
        res=[]
        inc, dec = 1, n
        for i in s:
            if i=='I':
                res+=[inc]
                inc+=1
            else:
                res+=[dec]
                dec-=1
        res+=[dec]
        return res

'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        if B==0:return[]
        
        elif B==1: return [1]
        m=A.count('D')
        res =list()
        count=m
        ctr=m+1
        res.append(ctr)
        ctr+=1
        for i in range(B-1):
            if A[i]=='D':
                res.append(count)
                count-=1
            else :
                res.append(ctr)

'''