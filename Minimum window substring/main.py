"""Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique."""
from collections import defaultdict

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def min_window(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n1 < n2: return ''
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        # update the hash_t
        for i in range(n2):
            c = t[i]
            hash_t[c] += 1
        l, count = 0, 0
        start_index = -1
        min_len = float('inf')
        # loop through the length of s
        for r in range(n1):
            # current right character
            c = s[r]
            hash_s[c] += 1
            # tracking the count to find the exact count needed
            if c in hash_t and hash_s[c] <= hash_t[c]:
                count += 1
            if count == n2:
                while s[l] not in hash_t or hash_s[s[l]] > hash_t[s[l]]:
                    # current left character
                    l_c = s[l]
                    hash_s[l_c] -= 1
                    l += 1
                window_len = r - l + 1
                if min_len > window_len:
                    min_len = window_len
                    start_index = l
        if start_index == -1: return ''
        return s[start_index: start_index + min_len]


solution = Solution()
result = solution.min_window(s='ADOBECODEBANC', t='ABC')
print(result)
