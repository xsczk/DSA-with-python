"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

- F(0) = 0, F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n)."""
from collections import defaultdict

# recursion
# memoization
class Solution:
    def __init__(self):
        self.memo = defaultdict(int)

    def fib(self, n: int) -> int:
        if n in self.memo: return self.memo[n]
        if n < 2:
            self.memo[n] = n
        else:
            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

fib = Solution()
num = fib.fib(10)
print(num)