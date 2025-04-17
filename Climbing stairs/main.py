"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

"""
from collections import defaultdict


class Solution:
    def __init__(self):
        self.memo = defaultdict(int)

    def climb_stairs(self, n: int) -> int:
        if n in self.memo: return self.memo[n]
        if n <= 3:
            self.memo[n] = n
        else:
            # there are f(n-1) + f(n-2) ways to reach the top from n steps (f(n))
            # because from f(n-1) we can climb 1 more step to reach f(n) or
            # from f(n - 2) we can climb 2 more step to reach f(n)
            self.memo[n] = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)
        return self.memo[n]
