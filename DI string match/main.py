"""
A permutation perm of n + 1 integers of all the integers in the range [0, n]
can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it.
If there are multiple valid permutations perm, return any of them.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'I' or 'D'.
"""

class Solution:
    # ad-hoc
    # time complexity: O(n)
    # space complexity: O(1)
    def di_string_match(self, s: str) -> list[int]:
        n = len(s)
        l, r = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        return ans + [r]