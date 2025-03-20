"""Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Note: An anagram is a word or phrase formed
by rearranging the letters of a different word or phrase,
using all the original letters exactly once.
"""
from collections import defaultdict


class Solution:
    # Time complexity: O(n * mlog(m)) - n is the length of strs, m is the length of the s
    # Space complexity: O(n)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        m = defaultdict(list)
        for s in strs:
            # every anagrams have only one version of sorted string
            hashed = ''.join(sorted(s))
            m[hashed].append(s)
        return [ls for ls in m.values()]

    # Time complexity: O(n * k)
    # Space complexity: O(n * k)
    def frequency_group_anagrams(self, strs: list[str]) -> list[list[str]]:
        m = defaultdict(list)
        for s in strs:
            # 26 characters from a -> z
            c_count = [0] * 26
            for c in s:
                # calc the frequency of character
                # from a to z present in the s
                c_count[ord(c) - ord('a')] += 1
            m[tuple(c_count)].append(s)
        return [ls for ls in m.values()]

solution = Solution()
result = solution.frequency_group_anagrams(strs=["eat","tea","tan","ate","nat","bat"])
print(result)