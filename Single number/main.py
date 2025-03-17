"""Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity
and use only constant extra space."""
from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def missing_number(self, nums: list[int]) -> int | None:
        count = Counter(nums)
        for (elem, cnt) in count.items():
            if cnt == 1: return elem

    # Time complexity: O(n)
    # Space complexity: O(n)
    def better_missing_number(self, nums: list[int]) -> int:
        total = sum(nums)
        uniq_nums = set(nums)
        double_elements_sum = 2 * sum(uniq_nums)
        return double_elements_sum - total

    # Time complexity: O(n)
    # Space complexity: O(1)
    def optimal_missing_number(self, nums: list[int]) -> int:
        """same_num ^ same_num = 0; 0 ^ single_num = single_num"""
        xor = 0
        for num in nums:
            """equivalent to xor = xor ^ num"""
            xor ^= num
        return xor

solution = Solution()
result = solution.optimal_missing_number([1, 2, 2, 1, 3, 4, 3])
print(result)