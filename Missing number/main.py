"""Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array."""

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)
        # Gauss formula
        sum_from_one_to_n = int((n * (n+1)) / 2)
        actual_sum = sum(nums)
        return sum_from_one_to_n - actual_sum

solution = Solution()
missing = solution.missing_number([9,6,4,2,3,5,7,0,1])
print(missing)