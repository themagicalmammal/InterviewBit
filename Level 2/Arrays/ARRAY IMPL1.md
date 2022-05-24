Predict the output of the following program :

```python
def performOps(A):
blen = 2 * len(A)
B = \[0\]\*blen
for i in xrange(len(A)):
B\[i\] = A\[i\]
B\[i + len(A)\] = A\[(len(A) - i) % len(A)\]
return B

Lets say performOps was called with A : \[5, 10, 2, 1\]. What would be the output of the following call :

B = performOps(A)
for i in xrange(len(B)):
print B\[i\],

```

<b> Ans - </b>  5 10 2 1 5 1 2 10
