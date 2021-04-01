'''

Problem Description

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.



Input Format
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.



Output Format
Return an Integer, i.e minimum number of steps.



Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

 '''

class Solution:
    def coverPoints(self, A, B):
        total = 0
        for i in range(len(A) - 1):
            b = B[i] - B[i+1]
            a = A[i] - A[i+1]
            total += max(abs(a),abs(b))
        return total

'''

class Solution:
    def coverPoints(self, A, B):
        steps = 0
        for i in range(len(A)-1):
            pt1 = (A[i],B[i])
            pt2 = (A[i+1],B[i+1])
            distance = self.distanceBtwnPoints(pt1,pt2)
            steps += distance            
        return steps
        
    def distanceBtwnPoints(self, pt1, pt2):
        return max(abs(pt1[0]-pt2[0]), abs(pt1[1]-pt2[1]))

'''