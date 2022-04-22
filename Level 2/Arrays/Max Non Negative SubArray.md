'''

Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

Problem Constraints
1 \<= N \<= 105
-109 \<= A\[i\] \<= 109

Input Format
The first and the only argument of input contains an integer array A, of length N.

Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.

Example Input
Input 1:

A = \[1, 2, 5, -7, 2, 3\]
Input 2:

A = \[10, -1, 2, 3, -4, 100\]

Example Output
Output 1:

\[1, 2, 5\]
Output 2:

\[100\]

Example Explanation
Explanation 1:

The two sub-arrays are \[1, 2, 5\] \[2, 3\].
The answer is \[1, 2, 5\] as its sum is larger than \[2, 3\].
Explanation 2:

The three sub-arrays are \[10\], \[2, 3\], \[100\].
The answer is \[100\] as its sum is larger than the other two.

NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

'''

class Solution:
def maxset(self, A):
r = 0
i = 0
x = 0
y = 0
c = 0
e = 0
f = 0
for i in range(len(A)):
if A\[i\] > -1:
r += A\[i\]
y = i
if r > c or r == c and f - e \< y - x:
c = r
e = x
f = y
else:
r = 0
x = i + 1
if A\[e\] > -1:
return A\[e:f + 1\]
return \[\]

'''

class Solution:
def maxset(self, A):
maxsumlist = \[\]
cursumlist = \[\]
maxsum = 0
currsum = 0
for i in A:
if (i >= 0):
currsum = currsum + i
cursumlist.append(i)
if(currsum > maxsum):
maxsum = currsum
maxsumlist = cursumlist
elif(currsum == maxsum):
if(len(cursumlist) > len(maxsumlist)):
maxsumlist = cursumlist
elif(i\<0):
currsum = 0
cursumlist = \[\]
return maxsumlist

'''
