What is the time complexity of the following code :

```python
    int a = 0, i = N;
    while (i > 0) {
        a += i;
        i /= 2;
    }
```

1. O(N)
1. O(Sqrt(N))
1. O(N / 2)
1. O(log N)
1. O(log(log N))

<b> Ans - </b> O(log N)

We have to find the smallest x such that `N / 2 ^ x < 1 OR 2 ^ x > N`

x = log(N)
