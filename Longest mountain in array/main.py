"""
You may recall that an array arr is a mountain array if and only if:

1. arr.length >= 3
2. There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain.
Return 0 if there is no mountain subarray.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4
"""


class Solution:
    def longest_mountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = start = 0
        while start < n:
            end = start
            # detect if there is any peak of a mountain
            while end + 1 < n and arr[end] < arr[end + 1]:
                end += 1
            # found the peak value
            if end > start:
                peak = end
                while end + 1 < n and arr[end] > arr[end + 1]:
                    end += 1
                if end != peak:
                    ans = max(ans, end - start + 1)
                start = end
            # if not, it means the end of array or not a valid peak found,
            # start again with start = end + 1
            else:
                start = end + 1
        return ans
