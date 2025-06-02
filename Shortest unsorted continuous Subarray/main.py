"""
Given an integer array nums, you need to find one continuous subarray such that
if you only sort this subarray in non-decreasing order, then the whole array
will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def find_unsorted_subarray(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1
        # find the initial boundaries of the unsorted subarray
        while start + 1 <= end and nums[start + 1] >= nums[start]:
            start += 1
        while end - 1 >= start and nums[end - 1] <= nums[end]:
            end -= 1
        # if the array is already sorted
        if start == end:
            return 0
        # find the min and max values in the unsorted subarray
        min_value, max_value = min(nums[start:end + 1]), max(
            nums[start:end + 1])
        # expand the boundaries to include all elements that are out of place
        while start > 0 and nums[start - 1] > min_value:
            start -= 1
        while end < len(nums) - 1 and nums[end + 1] < max_value:
            end += 1
        return end - start + 1
