"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".
Given the starting string start and the ending string result,
return True if and only if there exists a sequence of moves to transform start to result.

Constraints:
- 1 <= start.length <= 10^4
- start.length == result.length
- Both start and result will only consist of characters in 'L', 'R', and 'X'.
"""


class Solution:
    def can_transform(self, start: str, result: str) -> bool:
        # The frequency of 'X', 'R', and 'L' should be the same
        # in both the start and result strings
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1
            if i < n and j < n:
                if start[i] != result[j]:
                    return False
                # ensure that the index of 'L' in start is not less than its index
                # in result, as 'L' cannot move to the right. (LX cannot be XL)
                if start[i] == "L" and i < j:
                    return False
                # 'R' cannot move to the left (XR cannot be RX)
                if start[i] == "R" and j < i:
                    return False
                i += 1
                j += 1
        # ensure both start and result don't have any non-X characters on the rest
        while i < n:
            if start[i] != "X":
                return False
            i += 1
        while j < n:
            if result[j] != "X":
                return False
            j += 1
        return True
