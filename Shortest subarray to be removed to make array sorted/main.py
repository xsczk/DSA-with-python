"""Given an integer array arr, remove a subarray (can be empty)
from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array."""

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def find_length_of_the_shortest_array(self, arr: list[int]) -> int:
        n = len(arr)
        l = 0
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        if l == n - 1:
            return 0
        r = n - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        # find the minimum element to be remove first by comparing l and r:
        remove = min(n - 1 - l, r)
        # compare the last element in the prefix and the first element in the suffix
        # to find the actual result
        i, j = 0, r
        while i <= l and j < n:
            if arr[i] <= arr[j]:
                remove = min(remove, j - i - 1)
                i += 1
            else:
                j += 1
        return remove


solution = Solution()
result = solution.find_length_of_the_shortest_array(arr=[1, 2, 3, 10, 4, 2, 3, 5])
print(result)
