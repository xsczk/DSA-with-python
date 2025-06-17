"""
You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part. For example, the string "ababcc" can be
partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"]
are invalid.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""


class Solution:
    # two pointers, find the last index to update the partition boundaries
    # time complexity: O(n)
    # space complexity: O(n) - worst case. Ex: abcdef -> the answer is [1, 1, 1, 1, 1, 1]
    def partition_labels(self, s: str) -> list[int]:
        last_occurrence = 26 * [0]
        # find the last index of each character's occurrence in the s
        for i, c in enumerate(s):
            last_occurrence[ord(c) - ord('a')] = i
        # start & end to track the start and end points of the current partition
        start, end = 0, 0
        ans = []
        for i, c in enumerate(s):
            last_index = last_occurrence[ord(c) - ord('a')]
            # update the end pointer aka the boundary of the current partition
            if last_index > end:
                end = last_index
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans
