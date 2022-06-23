Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A\[i\] - A\[j\] = k, i != j.

Example:

Input :

```
A : [1 3 5] 
k : 4
```

Output : YES

as 5 - 1 = 4

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.

<b> Ans - </b>

```python
class Solution:
    def diffPossible(self, A, B):
        n = len(A)
        if n == 0:
            return 0
        i = 0
        j = 1
        while i < n and j < n:
            if i != j and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
        return 0
```

```python
class Solution:
    def diffPossible(self, A, B):
        import bisect

        for i in range(len(A) - 1):
            L = B + A[i]
            f = bisect.bisect_left(A, L, lo=i + 1, hi=len(A))
            if f < len(A) and A[f] == L:
                return 1
        return 0
```
