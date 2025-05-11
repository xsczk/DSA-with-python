"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the elements
that should be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.

Constrains:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9
"""


class Solution:
    # two pointers, iterate through from the end
    # Time complexity: O(m + n) - worst case if the smallest element in nums1
    # are greater than the greatest element in nums2
    # Space complexity: O(1)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1 # point to the last index in nums1
        p1 = m - 1 # point to the last element in the first m elements in nums1
        p2 = n - 1 # point to the last element in nums2
        # loop until p2 == -1 to handle the worst case
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        print(nums1)


solution = Solution()
solution.merge(nums1=[7, 8, 9, 0, 0, 0], nums2=[2, 5, 6], m=3, n=3)
