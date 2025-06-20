"""
Given an integer array nums and two integers left and right,
return the number of contiguous non-empty subarrays such that
the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= left <= right <= 10^9
"""
from typing import List


class Solution:
    # the answer will be the number of subarray can be formed
    # if all elements less than or equal to right
    # minus the number of subarray with all elements less than or equal to left - 1

    # time complexity: O(n)
    # space complexity: O(1)
    def num_subarray_bounded_max(self, nums: List[int], left: int,
                                 right: int) -> int:
        def num_subarray(bound: int) -> int:
            """return the number of subarrays can be formed
            with all elements less than or equal to bound"""
            ans, count = 0, 0
            for num in nums:
                count = count + 1 if num <= bound else 0
                ans += count
            return ans

        # the ans will be the number of subarray can be formed if all elements less than right
        # minus the number of subarray with all less than left - 1
        return num_subarray(right) - num_subarray(left - 1)
