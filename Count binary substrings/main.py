"""
Given a binary string s, return the number of non-empty substrings
that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings
are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""


class Solution:
    # group by character
    # time complexity: O(n)
    # space complexity: O(n)
    def count_binary_substrings(self, s: str) -> int:
        group = []
        count = 1
        # build a list of group
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                group.append(count)
                count = 1
        # append the count of last consecutively group
        group.append(count)
        # 00011 -> 2 valid substrings; 1110000 -> 3 valid substrings
        ans = 0
        for i in range(1, len(group)):
            ans += min(group[i], group[i - 1])
        return ans

    # linear scan based on above approach without using group list
    # time complexity: O(n)
    # space complexity: O(1)
    def count_binary_substrings_2(self, s: str) -> int:
        # keep track the previous and current group of consecutive 0 or 1
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        # plus the last valid substrings
        return ans + min(prev, cur)
