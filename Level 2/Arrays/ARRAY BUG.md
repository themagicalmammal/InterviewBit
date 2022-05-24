The following code is supposed to rotate the array A by B positions.

So, for example,

A : \[1 2 3 4 5 6\]

B : 1

The output :

\[2 3 4 5 6 1\]

However, there is a small bug in the problem. Fix the bug and submit the problem.

<b>NOTE:</b> You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

```python
class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            ret.append(a[i + b])
        return ret
```

```C++
vector<int> Solution::rotateArray(vector<int> &A, int B) {
	vector<int> ret; 
	for (int i = 0; i < A.size(); i++) {
		ret.push_back(A[i + B]);
	}
	return ret; 
}
```

<b> Ans - </b>

```python
class Solution:
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret
```

```C++
vector<int> Solution::rotateArray(vector<int> &A, int B) {
	vector<int> ret; 
	for (int i = 0; i < A.size(); i++) {
		ret.push_back(A[(i + B)%A.size()]);
	}
	return ret; 
}
```
