"""
You are given two integer arrays nums1 and nums2 both of the same length.
The advantage of nums1 with respect to nums2 is the number of indices i
for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

Constraints:
- 1 <= nums1.length <= 10^5
- nums2.length == nums1.length
- 0 <= nums1[i], nums2[i] <= 10^9
"""


class Solution:
    # greedy, two pointers, sorting
    # time complexity: O(n * log n)
    # space complexity: O(n)
    def advantage_count(self, nums1: list[int], nums2: list[int]) -> list[int]:

        def sorted_with_indices(nums: list[int]):
            """
            :param nums: input list need to be sorted
            :return: [12, 24, 8, 32] => [(2, 8), (0, 12), (1, 24), (3, 32)]
            """
            sorted_nums = [(i, num) for i, num in enumerate(nums)]
            sorted_nums.sort(key=lambda x: x[1])
            return sorted_nums

        sorted_nums1 = sorted_with_indices(nums1)
        sorted_nums2 = sorted_with_indices(nums2)

        i = 0
        # assigned is the list of nums1's value that is > nums2's value
        assigned = []
        # remaining is the list contains nums1's values that are not assigned to any values in nums2
        remaining = []
        for j, num in sorted_nums2:
            while i < len(nums1) and sorted_nums1[i][1] <= num:
                remaining.append(sorted_nums1[i])
                i += 1
            if i < len(nums1):
                assigned.append(sorted_nums1[i])
            i += 1

        # append remaining to the end of assigned as remaining is useless for the answer
        assigned = assigned + remaining
        combined = list(zip(assigned, sorted_nums2))
        # reconstruct the element in nums1 based on the original order of nums2
        combined.sort(key=lambda x: x[1][0])
        return [x[0][1] for x in combined]

    # greedy, two pointers, hash table, sorting
    # time complexity: O(n * log n)
    # space complexity: O(n)
    def advantage_count_2(self, nums1: list[int], nums2: list[int]) -> list[
        int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in nums2}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sorted_nums2[j] is always the smallest unassigned element in nums2
        j = 0
        for a in sorted_nums1:
            if a > sorted_nums2[j]:
                assigned[sorted_nums2[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        # reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in nums2]



solution = Solution()
print(solution.advantage_count_2(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11]))
