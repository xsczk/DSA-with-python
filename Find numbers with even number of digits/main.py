"""Given an array nums of integers, return how many of them contain an even number of digits."""

class Solution:
    def find_numbers(self, nums: list[int]) -> int:
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt