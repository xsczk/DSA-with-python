"""
Given an integer array nums, move all the even integers at the beginning of the array
followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""


class Solution:
    # two pointers
    # time complexity: O(n) - worst case
    # space complexity: O(1)
    def sort_array_by_parity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            while l < n and nums[l] % 2 == 0:
                l += 1
            while r >= 0 and nums[r] % 2 != 0:
                r -= 1
            if l >= r:
                break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
