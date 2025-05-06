"""Given two strings needle and haystack, return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack."""

class Solution:
    # sliding window
    # Time complexity: O(m * n)
    # Space complexity: O(1)
    def str_str(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        # base case
        if m < n:
            return -1
        for i in range(m):
            if needle == haystack[i:i + n]:
                return i
        return -1