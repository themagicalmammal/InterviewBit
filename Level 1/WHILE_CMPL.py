'''

What is the time complexity of the following code :

        int a = 0, i = N;
        while (i > 0) {
            a += i;
            i /= 2;
        }

 O(N)
 O(Sqrt(N))
 O(N / 2)
 O(log N)
 O(log(log N))

'''

O(log N)

We have to find the smallest x such that `N / 2^x < 1 OR 2^x > N`

x = log(N) 