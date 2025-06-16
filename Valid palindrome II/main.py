"""
Given a string s, return true if the s can be palindrome
after deleting at most one character from it.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""


class Solution:
    # two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    def valid_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def is_palindrome(i: int, j: int) -> bool:
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        while left < right:
            if s[left] != s[right]:
                # delete either one character from left or right
                return (is_palindrome(left, right - 1) or
                        is_palindrome(left + 1, right))
            left, right = left + 1, right - 1
        return True

    def valid_palindrome_2(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # delete either one character from left or right
                skip_left, skip_right = s[left + 1: right + 1], s[left:right]
                return (skip_left == skip_left[::-1] or
                        skip_right == skip_right[::-1])
            left, right = left + 1, right - 1
        return True
