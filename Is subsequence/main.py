"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""
from collections import defaultdict


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


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
# and you want to check one by one to see if t has its subsequence.
# In this scenario, how would you change your code?

# dynamic programing with binary search
class SubsequenceChecker:
    def is_subsequence(self, s: str, t: str) -> bool:
        char_indices = defaultdict(list)
        for i, char in enumerate(t):
            char_indices[char].append(i)
        pos = -1
        for c in s:
            if c not in char_indices:
                return False
            idx_ls = char_indices[c]
            # find the first index in idx_ls such that index > pos
            i = self.binary_search(current_position=pos, indices_list=idx_ls)
            if i == len(idx_ls):
                # that means idx_ls[i] < pos => invalid to continue traversing
                return False
            pos = idx_ls[i]
        return True

    # method to find the first index in the list where the value > current_position
    # indices_list is already sorted
    # Time complexity: O(log n)
    def binary_search(self, current_position: int, indices_list: list[int]) -> int:
        l, r = 0, len(indices_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if indices_list[mid] > current_position:
                # reduce r pointer to keep finding smaller index that greater than current_pos
                r = mid - 1
            else:
                l = mid + 1
        return l


checker = SubsequenceChecker()
ans = checker.is_subsequence('ahj', 'bcgkeheajk')
print(ans)
