'''

Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Look at the example for more details.

Example

A = 5
Return: [1 2 Fizz 4 Buzz]

'''


class Solution:
    def fizzBuzz(self, A):
        a = [i + 1 for i in range(A)]
        for i in range(2, A, 3):
            a[i] = 'Fizz'
        for i in range(4, A, 5):
            a[i] = 'Buzz'
        for i in range(14, A, 15):
            a[i] = 'FizzBuzz'
        return a
