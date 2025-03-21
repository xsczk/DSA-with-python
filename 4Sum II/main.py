"""Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
 return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0"""
from collections import defaultdict

# Time complexity: O(n^2)
# Space complexity: O(n^2)
class Solution:
    def four_sum_count(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        m = defaultdict(int)
        count = 0
        for a in nums1:
            for b in nums2:
                m[a + b] += 1

        for c in nums3:
            for d in nums4:
                if -c - d in m:
                    count += m[-c - d]
        return count


solution = Solution()
result = solution.four_sum_count(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
print(result)
