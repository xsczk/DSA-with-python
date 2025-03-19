"""Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct."""

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def is_duplicate(self, nums: list[int]) -> bool:
        m = {}
        for num in nums:
            if num in nums:
                return True
            m[num] += 1
        return False


solution = Solution()
result = solution.is_duplicate([1, 2, 9, 4, 2])
print(result)
