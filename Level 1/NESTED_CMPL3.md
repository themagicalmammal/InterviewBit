What is time complexity of following code :

```python
    int count = 0;
    for (int i = N; i > 0; i /= 2) {
        for (int j = 0; j < i; j++) {
            count += 1;
        }
    }
```

1. O(N * N)
1. O(N * log N)
1. O(N * log(log(N)))
1. O(N)
1. O(N * Sqrt(N))


<b> Ans - </b> O(N)

In the first iteration, the j loop runs N times.

In the second iteration, the j loop runs N / 2 times.

In the ith iteration, the j loop runs N / 2 ^ i times.

So, the total number of runs of loop = N + N / 2 + N / 4 + ... 1

= **N * (1 + 1 / 2 + 1 / 4 + 1 / 8 + ...) \< 2 * N**
