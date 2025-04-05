"""Given two integers n and k,
return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order."""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        # will start at index 1 because we want to find result
        # based on the range from [1,n]
        def backtrack(cur=[], index = 1):
            # base case
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(index, n + 1):
                cur.append(i)
                backtrack(cur, i + 1)
                cur.pop()
        backtrack()
        return ans

solution = Solution()
ans = solution.combine(4, 2)
print(ans)