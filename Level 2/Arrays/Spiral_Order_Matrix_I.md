Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[ <br />
[ 1, 2, 3 ], <br />
[ 4, 5, 6 ], <br />
[ 7, 8, 9 ] <br />
]

You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]

<b> Ans - </b>

```python
class Solution:
    def spiralOrder(self, A):
        lst = []
        t = 0
        b = len(A) - 1
        l = 0
        r = len(A[0]) - 1
        dir = 0
        while(t <= b and l <= r):
            if(dir == 0):
                for i in range(l,r+1):
                    lst.append(A[t][i])
                t += 1
            elif(dir == 1):
                for i in range(t,b+1):
                    lst.append(A[i][r])
                r -= 1
            elif(dir == 2):
                for i in range(r,l-1,-1):
                    lst.append(A[b][i])
                b -= 1
            elif (dir == 3):
                for i in range(b,t-1,-1):
                    lst.append(A[i][l])
                l += 1
            dir = (dir + 1) % 4
        return lst

```
```python
class Solution:
    def spiralOrder(self, A):
        l = []

        R = len(A)
        C = len(A[0])

        total_levels = min(R, C)//2

        for level in range(total_levels):
            l.extend(A[level][level: C - level])

            for row_no in range(level+1, R - level):
                l.append(A[row_no][C-level-1])
            
            l.extend((A[R-level-1][level: C-level-1])[::-1])

            for row_no in range(R-level-2, level, -1):
                l.append(A[row_no][level])

        if R <= C and R%2 == 1:
            l.extend(A[total_levels][total_levels: C - total_levels])
        elif R > C and C%2 == 1:
            for row_no in range(total_levels, R - total_levels):
                l.append(A[row_no][total_levels])

        return l
```

```C++
vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
    int dir = 0;
    vector<int> B;
    int m = A.size();
    int n = A[0].size();
    int t=0, l=0, b = m-1, r=n-1;
    while(t<=b && l<=r){
        if(dir==0){
            for(int i=l; i<=r; i++){
                B.push_back(A[t][i]);
            }
            t++;
            dir=1;
        }
        else if(dir==1){
            for(int i=t; i<=b; i++){
                B.push_back(A[i][r]);
            }
            r--;
            dir=2;
        }
        else if(dir==2){
            for(int i=r; i>=l; i--){
                B.push_back(A[b][i]);
            }
            b--;
            dir=3;
        }
        else if(dir==3){
            for(int i=b; i>=t; i--){
                B.push_back(A[i][l]);
            }
            l++;
            dir=0;
        }
        else break;
    }
    return B;
}
```

