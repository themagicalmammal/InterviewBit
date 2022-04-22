'''

Given a number N, find all prime numbers up to N ( N included ).

Example:

if N = 7,

all primes till 7 = {2, 3, 5, 7}

Make sure the returned array is sorted.

Problem Approach:

Complete code in the hint.

'''

class Solution:
def sieve(self, A):
size = A // 2
sieve = \[1\] * size
for i in range(1, int(A\*\*0.5)):
if sieve\[i\]:
val = 2 * i + 1
tmp = (size - i - 1) // val
sieve\[i + val::val\] = \[0\] * tmp
return \[2\] + \[i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0\]
