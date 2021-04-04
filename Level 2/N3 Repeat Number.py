'''

You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

'''

import random
class Solution:
    def repeatedNumber(self, nums):
        n = len(nums)
        for i in range(20):
            j = random.choice(nums)
            if nums.count(j) > n//3: return j
        return -1