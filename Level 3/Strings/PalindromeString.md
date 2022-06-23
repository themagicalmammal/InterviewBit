Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

Check the sample test case for reference.

Example:

Input 1:

"A man, a plan, a canal: Panama"

Input 2:

"race a car"

Output and Explanation 1:

1

The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" which is a palindrome after ignoring the case.

Output and Explanation 2:

0

The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

<b> Ans - </b>

```python
import string
import hashlib


class Solution:
    def isPalindrome(self, A):
        if not A:
            return 0

        trt = A.maketrans("", "", string.punctuation)
        A = A.translate(trt).replace(" ", "").lower()

        s_b = bytearray(A[: len(A) // 2], "utf-8")
        e_b = bytearray(A[len(A) - len(A) // 2 :], "utf-8")

        e_b.reverse()

        start = hashlib.md5(s_b)
        end = hashlib.md5(e_b)
        if start.hexdigest() == end.hexdigest():
            return 1
        return 0
```
