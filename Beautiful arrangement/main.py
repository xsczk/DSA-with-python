"""Suppose you have n integers labeled 1 through n.
A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement
if for every i (1 <= i <= n), either of the following is true:

- perm[i] is divisible by i.
- i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct."""


class Solution:
    def __init__(self):
        self.count = 0

    def count_arrangement(self, n: int) -> int:
        visited = [False] * (n + 1)

        def backtrack(i: int):
            # base case
            if i > n:
                self.count += 1
                return
            for j in range(1, n + 1):
                if not visited[j] and (j % i == 0 or i % j == 0):
                    # mark j as visited
                    visited[j] = True
                    # recursive to check in the next index
                    backtrack(i + 1)
                    # backtrack
                    visited[j] = False

        backtrack(1)
        return self.count


solution = Solution()
ans = solution.count_arrangement(3)
print(ans)
