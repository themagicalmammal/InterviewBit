Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:

The first and the only argument contains an integer, A.

Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.

Constraints:

1 \<= A \<= 1000

Examples:

Input 1:<br />
A = 3

Output 1: <br />
\[   \[ 1, 2, 3 \], <br />
\[ 8, 9, 4 \], <br />
\[ 7, 6, 5 \]   \]

Input 2:<br />
4

Output 2: <br />
\[   \[1, 2, 3, 4\], <br />
\[12, 13, 14, 5\], <br />
\[11, 16, 15, 6\], <br />
\[10, 9, 8, 7\]   \]

<b> Ans - </b>

```python
class Solution:
    def generateMatrix(self, A):
        result = [[0] * (A) for _ in range(A)]

        max_x = max_y = (A) - 1
        start_x = start_y = 0
        i = 1
        while i <= (A) ** 2:
            for j in range(start_y, max_y + 1):
                result[start_x][j] = i
                i += 1
            start_x += 1

            for j in range(start_x, max_x + 1):
                result[j][max_y] = i
                i += 1
            max_y -= 1

            for j in range(max_y, start_y - 1, -1):
                result[max_x][j] = i
                i += 1
            max_x -= 1

            for j in range(max_x, start_x - 1, -1):
                # print(i, j, max_x, start_x-1, result)
                result[j][start_y] = i
                # print(result)
                i += 1
            start_y += 1
        return result
```
