'''

Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is found else return -1.



Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1


Example Explanation
Explanation 1:

 For integer 2, there are 2 greater elements in the array. So, return 1.
Explanation 2:

 There is no such integer exists.

'''

class Solution:
    def solve(self, A):
        A.sort(reverse=True)
        if A[0] == 0:
            return 1
        for i in range(len(A)):
            if A[i-1] != A[i] and A[i] == i:
                return 1
        return -1

'''

class Solution:
  def solve(self, array):
      offset=0
      while len(array)>0:
        p=array[0]
        bigger=[]
        smaller=[]
        same=0
        for i in array[1:]:
          if i>p:
            bigger+=[i]
          elif i<p:
            smaller+=[i]
          else:
            same+=1
        if p>len(bigger)+offset:
          array=smaller
          offset+=len(bigger)+same+1
        elif p<len(bigger)+offset:
          array=bigger
        else:
          return 1
      return -1
    
'''