"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""


class Solution:
    # two pointers
    # Time complexity: O(len(t))
    # Space complexity: O(1)
    def is_subsequence(self, s: str, t: str) -> bool:
        # define two pointers, one is the pointer of s, the other is the pointer of t
        sp = tp = 0
        # we can traverse string t and identify all the characters it contains.
        while tp < len(t) and sp < len(s):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        # sp == len(s) which means all the characters in s are represented in the same order of t
        return sp == len(s)

