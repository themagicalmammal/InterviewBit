'''

Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]

'''


class Solution:
    def spiralOrder(self, a):
        rows = len(a)
        cols = len(a[0])
        ret = []
        t = 0
        b = rows - 1
        l = 0
        r = cols - 1
        dir = 0
        while t <= b and l <= r:
            if dir == 0:
                for i in range(l, r + 1):
                    ret.append(a[t][i])
                t += 1
                dir = 1
            elif dir == 1:
                for i in range(t, b + 1):
                    ret.append(a[i][r])
                r -= 1
                dir = 2
            elif dir == 2:
                for i in range(r, l - 1, -1):
                    ret.append(a[b][i])
                b -= 1
                dir = 3
            elif dir == 3:
                for i in range(b, t - 1, -1):
                    ret.append(a[i][l])
                l += 1
                dir = 0
        return ret


'''

class Solution:
    def spiralOrder(self, A):
        L = 0
        R = len(A[0]) -1
        B = len(A) -1
        T = 0
        dir = 0
        res = []
        while T <= B and L <= R:
            if dir == 0:
                for i in range(L, R+1):
                    res.append(A[T][i])
                T += 1
            elif dir == 1:
                for i in range(T, B+1):
                    res.append(A[i][R])
                R -= 1
            elif dir == 2:
                for i in range(R, L-1, -1):
                    res.append(A[B][i])
                B -= 1
            else:
                for i in range(B, T-1, -1):
                    res.append(A[i][L])
                L += 1
            dir = (dir+1) % 4
        return res

'''
