"""
Given a string s and a character c that occurs in s,
return an array of integers answer where answer.length == s.length
and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Constraints:
- 1 <= s.length <= 10^4
- s[i] and c are lowercase English letters.
- It is guaranteed that c occurs at least once in s.
"""


class Solution:
    # traverse twice
    # time complexity: O(n)
    def shortest_to_char(self, s: str, c: str) -> list[int]:
        ans, n = [0] * len(s), len(s)
        prev = float("-inf")
        # traverse left to right, keep track the most recent i of c and update ans[i]
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        prev = float("inf")
        # traverse from right to left, applying the same logic as before,
        # but update ans[i] to be the smaller value between its current value and prev - i.
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(prev - i, ans[i])
        return ans
