"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order."""

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            if m.get(num) is not None:
                return [m.get(num), i]
            m[target - num] = i


solution = Solution()
result = solution.two_sum([3, 2, 4], target=6)
print(result)
