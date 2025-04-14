"""Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""


class Solution:
    def combination_sum_2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        def backtrack(cur: list[int], i: int, cur_sum: int):
            if cur_sum == target:
                ans.append(cur[:])
                return
            for j in range(i, len(candidates)):
                # skip next recursive call if duplicates or next current sum > target
                if (cur_sum + candidates[j] > target or
                        (j > i and candidates[j] == candidates[j - 1])): continue
                cur.append(candidates[j])
                backtrack(cur, j + 1, cur_sum + candidates[j])
                cur.pop()
        backtrack(cur=[], i=0, cur_sum=0)
        return ans


solution = Solution()
ans = solution.combination_sum_2([3,1,3,5,1,1], 8)
print(ans)
