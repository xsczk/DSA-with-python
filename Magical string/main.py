"""A magical string s consists of only '1' and '2' and obeys the following rules:

The string s is magical because concatenating the number of contiguous occurrences
of characters '1' and '2' generates the string s itself.
The first few elements of s is s = "1221121221221121122……".
If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......"
and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......".
You can see that the occurrence sequence is s itself.

Given an integer n, return the number of 1's in the first n number in the magical string s.

Constraints: 1 <= n <= 10^5
"""

class Solution:
    # two pointers, build the magical string from scratch
    def magical_string(self, n: int) -> int:
        # initialize the magical string with 3 elements
        s = [1, 2, 2]
        # use index to track the position in the string for generating the next elements
        i = 2
        while len(s) < n:
            # get the last value in the magical string
            last = s[-1]
            # next value to append is the opposite of the last value
            # there will be max 2 elements in each group 1 or 2
            next = 3 - last
            # s[i] is the number of occurrences of the next character in s
            s += [next] * s[i]
            i += 1
        # count the number of 1 in the first n elements of s
        return s[:n].count(1)

solution = Solution()
magical_str = solution.magical_string(8)

