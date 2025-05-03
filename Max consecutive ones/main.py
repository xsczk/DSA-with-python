"""Given a binary array nums, return the maximum number
of consecutive 1's in the array."""

class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans