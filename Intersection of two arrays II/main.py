"""Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays,
and you may return the result in any order."""
from collections import Counter


class Solution:
    # hash table
    # Time complexity: O(n)
    # Space complexity: O(n)
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # get the counter for nums1
        count = Counter(nums1)
        ans = []
        for num in nums2:
            if count.get(num, 0):
                ans.append(num)
                count[num] -= 1
        return ans
