"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing
in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer,
but it does not fit in 32-bit integer, return -1.

Constraints:
- 1 <= n <= 2^31 - 1
"""


class Solution:
    # Time complexity: O(k) - k is small, max 10 characters since n <= 2^31 -1
    # Space complexity: O(k)
    def next_greater_element(self, n: int) -> int:
        s = list(str(n))
        i = len(s) - 1
        # find the first decreasing element from the right
        while i - 1 >= 0 and s[i - 1] >= s[i]:
            i -= 1
        # it i at index 0, there is no valid answer
        if not i:
            return -1
        last_char_index = i - 1
        # reverse the remaining s start from index i
        l, r = i, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        i = len(s) - 1
        while i > 0 and s[i] > s[last_char_index]:
            i -= 1
        # swap the num at last_char_index with the num at index i + 1
        s[last_char_index], s[i + 1] = s[i + 1], s[last_char_index]
        res = int(''.join(s))
        # return the res based on notice section in the description
        return res if res <= 2 ** 31 - 1 else -1
