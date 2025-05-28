"""Given a string s and a string array dictionary, return the longest string in the dictionary
that can be formed by deleting some of the given string characters.
If there is more than one possible result, return the longest word
with the smallest lexicographical order. If there is no possible result,
return the empty string.

Constraints:
- 1 <= s.length <= 1000
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 1000
- s and dictionary[i] consist of lowercase English letters.
"""


class Solution:
    # Time complexity: O(n * k)
    # Space complexity: O(1)
    def find_longest_word(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(s: str, t: str) -> bool:
            """helper to check if s is a subsequence of t"""
            j = 0
            for i in range(len(t)):
                if j == len(s):
                    break
                if t[i] == s[j]:
                    j += 1
            return j == len(s)

        longest = ""
        for word in dictionary:
            if is_subsequence(word, s):
                # update result if longer subsequence
                # or subsequence with smaller lexicographical order is found
                if len(word) > len(longest) or (
                        len(word) == len(longest) and word < longest
                ):
                    longest = word
        return longest

