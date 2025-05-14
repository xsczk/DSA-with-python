"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Constraints:
- 1 <= s.length <= 104
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.
"""


class Solution:
    # two pointers
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverse_words(self, s: str) -> str:
        # split s into a list, separate by a space
        words = s.split(' ')
        l, r = 0, len(words) - 1
        while l < r:
            # skip empty character
            while words[l] == '':
                l += 1
            while words[r] == '':
                r -= 1
            if l >= r: break
            # swap left and right character
            temp = words[l]
            words[l] = words[r]
            words[r] = temp
            l += 1
            r -= 1
        # using list comprehension to connect each word together, exclude ''
        return ' '.join([word for word in words if word != ''])


solution = Solution()
reversed_words = solution.reverse_words(
    " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU")
print(reversed_words)
