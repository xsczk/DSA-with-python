"""Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.

"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(cur: list[int]):
            # base case
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                # len = 0 is the condition for init execution
                if len(cur) == 0 or nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
            return
        backtrack([])
        return ans

solution = Solution()
ans = solution.permute([1,2,3])
print(ans)