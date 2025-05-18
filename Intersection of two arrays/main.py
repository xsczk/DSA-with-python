"""Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order."""


class Solution:
    # hash table
    # Time complexity: O(n)
    # Space complexity: O(n)
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.add(nums1[i])
        return list(ans)

    # follow up: if both given array are sorted
    # two pointers, binary search
    # Time complexity: O(n)
    # Space complexity: O(1)
    def intersection_2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i, j = 0, 0
        ans = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(ans)


solution = Solution()
res = solution.intersection_2([1, 2, 2, 3], [2, 2, 3, 4])
print(res)
