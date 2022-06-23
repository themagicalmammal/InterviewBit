Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 

Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:

  (-1, 0, 1)

  (-1, -1, 2)
<b> Ans - </b>  

```python
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def threeSum(self, A):
        A=sorted(A)
        B = []
        prev=-10**11
        for i in range(len(A)-2):
            target= -A[i]
            j=i+1
            k=len(A)-1
            c=-10**11
            while j<k:
                c=A[j]+A[k]
                if c<target:
                    j=j+1
                elif c>target:
                    k=k-1
                else:
                    B.append([A[i], A[j], A[k]])
        return B
```

```python
class Solution:
    def threeSum(self, A):
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        if 0 in d and d[0]>2:
            res=[[0,0,0]]
        else:
            res=[]
        neg=[]
        pos=[]
        for i in d:
            if i<0:
                neg.append(i)
            elif i>0:
                pos.append(i)
        for p in pos:
            for n in neg:
                i=-p-n
                if i not in d:
                    continue
                elif i==0:
                    res.append([n,i,p])
                elif i==p and d[i]>1:
                    res.append([n,p,p])
                elif i==n and d[i]>1:
                    res.append([n,n,p])
                elif i>p:
                    res.append([n,p,i])
                elif i<n:
                    res.append([i,n,p])
        return res

```