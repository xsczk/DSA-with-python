"""Given a string s, find the length of the longest substring without duplicate characters.
"""


# Time complexity: O(n) - n is the length of the array
# Space complexity: O(n) - the map structure can hold all the character of the input (worst case)
class Solution:
    def length_of_the_longest_substring(self, s: str) -> int:
        str_len = len(s)
        seen = {}
        longest = 0
        l, r = 0, 0
        while l < str_len and r < str_len:
            curr = s[r]
            if curr in seen:
                prev_char_index = seen[curr]
                # using max to cover the case that start and end character
                # are the same and l is not at 0
                l = max(l, prev_char_index + 1)
            seen[curr] = r
            longest = max(longest, r - l + 1)
            r += 1
        return longest

solution = Solution()
longest = solution.length_of_the_longest_substring('abcabcbba')

print(longest)
