"""
Given an array of integers nums, half of the integers in nums are odd,
and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd,
and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Constraints:
- 2 <= nums.length <= 2 * 10^4
- nums.length is even.
- Half of the integers in nums are even.
- 0 <= nums[i] <= 1000
"""

class Solution:
    def sort_array_by_parity_II(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i, j = 0, 1
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 != 0:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums