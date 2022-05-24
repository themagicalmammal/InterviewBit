'''

Given a number N, find all factors of N.

Example:

N = 6
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.

'''

class Solution:
def allFactors(self, A):
z = \[\]
for i in range(1, int(A\*\*0.5) + 1):
if A % i == 0:
z.extend(\[i, A // i\])
return sorted(set(z))

'''

class Solution:
def allFactors(self, A):
z = \[\]
for i in range(1, int(A\*\*0.5)+1):
if A%i == 0:
z.insert(-)
z.extend(\[i,A//i\])
return sorted(set(z))

OR

class Solution:
def allFactors(self, A):
factors = \[\]
factors2 = \[\]
\# brute force
for x in range(1, int(A\*\*0.5)+1):
d, m = divmod(A, x)
if m == 0:
factors.append(x)
if d != x:
factors2.append(d)
factors2.reverse()
return factors + factors2

'''
