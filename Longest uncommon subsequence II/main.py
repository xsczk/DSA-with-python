"""Given an array of strings strs, return the length of
the longest uncommon subsequence between them. If the longest uncommon subsequence
does not exist, return -1.

An uncommon subsequence between an array of strings is a string
that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained
after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because
you can delete "e" and "d" in "aebdc" to get "abc".
Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Constraints:
- 2 <= strs.length <= 50
- 1 <= strs[i].length <= 10
- strs[i] consists of lowercase English letters.
"""


class Solution:
    # sorting, two pointers
    # Time complexity: O(n^2 * m) where n is the len of strs, m is the max len of s in strs
    # Space complexity: O(1) excluding input
    def find_LUS_length(self, strs: list[str]) -> int:

        def is_subsequence(s1: str, s2: str) -> bool:
            """check if s1 is a subsequence of s2"""
            i = 0
            for c in s2:
                if i == len(s1):
                    return True
                if s1[i] == c:
                    i += 1
            return i == len(s1)

        # sort the strs in descending order by length
        strs.sort(key=lambda s: -len(s))
        # loop the strs and check each str to determine
        # if it's a subsequence of any other (skip itself)
        longest = -1
        for i, s1 in enumerate(strs):
            # skip the duplicate s1 for better performance
            if i + 1 < len(strs) and strs[i + 1] == s1:
                continue
            non_subsequence = True
            # check if s1 is a subsequence of any other
            for j, s2 in enumerate(strs):
                # skip checking itself
                if i == j:
                    continue
                # if subsequence is found, break the loop and continue checking for the next s1
                if is_subsequence(s1, s2):
                    non_subsequence = False
                    break
            # if s1 is not a subsequence of any other s in strs, update the longest
            if non_subsequence:
                longest = max(longest, len(s1))
        return longest


solution = Solution()
longest_len_of_non_subsequence = solution.find_LUS_length(
    ["aabbcc", "aabbcc", "bc", "bcc", "aabbccc"]
)
print(longest_len_of_non_subsequence)
