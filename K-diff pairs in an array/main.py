"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

- 0 <= i, j < nums.length
- i != j
- |nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Constraints:
- 1 <= nums.length <= 10^4
- -10^7 <= nums[i] <= 10^7
- 0 <= k <= 10^7
"""
from collections import Counter


class Solution:
    def find_pairs(self, nums: list[int], k: int) -> bool:
        count = Counter(nums)
        res = 0
        for num in count:
            if (k == 0 and count[num] >= 2) or (k != 0 and num + k in count):
                res += 1
        return res
