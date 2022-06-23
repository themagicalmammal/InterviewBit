Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.

Return the sum of the three integers.

Assume that there will only be one solution

Example:

given array S = {-1 2 1 -4},

and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
<b> Ans - </b>

```python
class Solution:
    def threeSumClosest(self, A, B):
        A = sorted(A)
        prev = -100000
        for i in range(len(A)):
            target = B - A[i]
            j = i + 1
            k = len(A) - 1
            c = -1000000
            while j < k:
                c = A[j] + A[k]
                if c < target:
                    j = j + 1
                elif c > target:
                    k = k - 1
                else:
                    return A[i] + c
            su = A[i] + c
            if abs(B - prev) > abs(B - su):
                prev = su
        return prev
```
