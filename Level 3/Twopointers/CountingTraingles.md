You are given an array of N non-negative integers, A0, A1 ,…, AN-1.

Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.

For example,

A = \[1, 1, 1, 2, 2\]

Return: 4

<b> Ans - </b>

```python
class Solution:
    def nTriang(self, A):
        arr = A
        n = len(arr)
        arr.sort()
        count = 0
        for i in range(0, n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n:
                    if arr[i] + arr[j] > arr[k]:
                        k += 1
                    else:
                        break
                count += k - j - 1
        return count % (1000000007)
```
