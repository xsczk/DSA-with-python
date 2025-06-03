"""
Given an integer array nums, return the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""


class Solution:
    # valid triangle when the length of any side is less than the sum of the other two sides.
    def triangle_number(self, nums: list[int]) -> int:
        # sort for using binary search
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(2, n):
            i, j = 0, k - 1
            # binary search
            while i < j:
                # in this case, moving i to the right always causes
                # nums[i] + nums[j] > nums[k] since k and j are fixed
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


solution = Solution()
print(solution.triangle_number([2, 2, 3, 4]))
