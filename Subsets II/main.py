"""Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

"""

# Time complexity: O(2^n)
# Space complexity: O(2^n)
class Solution:
    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        # sort the nums for easier skipping duplicates
        nums.sort()

        def backtrack(cur=[], index=0):
            ans.append(cur[:])
            for i in range(index, len(nums)):
                # if the indices of current loop is greater than index and
                # current element equal to previous element => skip
                if i > index and nums[i] == nums[i - 1]: continue
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()

        backtrack()
        return ans


solution = Solution()
ans = solution.subsets_with_dup([1, 2, 2])
print(ans)
