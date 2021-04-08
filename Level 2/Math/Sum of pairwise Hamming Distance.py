'''

Problem Description

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.



Problem Constraints
1 <= |A| <= 200000

1 <= A[i] <= 109



Input Format
First and only argument is array A.



Output Format
Return one integer, the answer to the problem.



Example Input
Input 1:

 A = [1]
Input 2:

 A = [2, 4, 6]


Example Output
Output 1:

 0
Output 2:

 8


Example Explanation
Explanation 1:

 No pairs are formed.
Explanation 2:

 We return, f(2, 2) + f(2, 4) + f(2, 6) + f(4, 2) + f(4, 4) + f(4, 6) + f(6, 2) + f(6, 4) + f(6, 6) = 8

'''

class Solution:
    def hammingDistance(self, A):
        array=[]
        total=0
        for i in A:
            array.append('{0:032b}'.format(i))
        array=list(zip(*array))
        for i in array:
            a=i.count("0")
            total+=2*a*(len(i)-a)
        return total%1000000007

'''

class Solution:
    def hammingDistance(self, A):
        ans = 0 
        for i in range(32): 
            count = 0
            for j in A: 
                if j & (1 << i): 
                    count += 1
            ans += (count * (len(A) - count) * 2); 
            ans %= 1000000007
        return ans 

'''