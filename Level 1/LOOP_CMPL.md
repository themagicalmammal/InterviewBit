'''

What is the time, space complexity of following code :

```
    int a = 0, b = 0;
    for (i = 0; i < N; i++) {
        a = a + rand();
    }
    for (j = 0; j < M; j++) {
        b = b + rand();
    }
```

Assume that rand() is O(1) time, O(1) space function.

O(N * M) time, O(1) space
O(N + M) time, O(N + M) space
O(N + M) time, O(1) space
O(N * M) time, O(N + M) space
O(N * M) time, O(N * M) space

'''

O(N + M) time, O(1) space

The first loop is O(N) and the second loop is O(M). Since you don't know which is bigger, you say \*\* this is O(N + M)\*\*. This can also be written as O(max(N, M)).

Since there is no additional space being utilised, the space complexity is constant / O(1)
