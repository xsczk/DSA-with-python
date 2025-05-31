"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""


class Solution:
    # Sliding window, hash table
    # Time complexity: O(len(s2))
    # Space complexity: O(1) - the frequency array has fixed-size of length 26 (alphabet letters)
    def check_inclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # there are 26 alphabet letters
        s1_count = [0] * 26
        window_count = [0] * 26
        # count the characters frequency represent in s1 and the first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == window_count:
            return True
        # sliding the window through s2
        for i in range(len(s1), len(s2)):
            # remove left most character count by 1
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # add new character at right most for each check
            window_count[ord(s2[i]) - ord('a')] += 1
            if window_count == s1_count:
                return True
        return False
