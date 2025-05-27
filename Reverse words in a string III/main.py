"""Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Constraints:
- 1 <= s.length <= 5 * 104
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.
"""


class Solution:
    # iterative and reverse each word
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverse_words(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)

    # Time complexity: O(n)
    # Space complexity: O(n) due to result list
    def reverse_words_2(self, s: str) -> str:
        last_space_index = -1
        result = []
        for str_index in range(len(s)):
            # if we are currently at the last of the s or current character is a space
            if s[str_index] == ' ' or str_index == len(s) - 1:
                last_character = str_index - 1 if s[str_index] == ' ' else str_index
                # reverse each word
                for c_index in range(last_character, last_space_index, -1):
                    result += s[c_index]
                if str_index != len(s) - 1:
                    result += ' '
                # assign last_space_index to str_index since the first index of the character
                # of the next word will be last_space_index + 1 for the next iteration
                last_space_index = str_index
        return ''.join(result)

    # Two pointers based on approach above
    # Time complexity: O(n)
    # Space complexity: O(n) due to converting s to a list
    def reverse_words_3(self, s: str) -> str:
        last_space_index = -1
        s = list(s)
        for str_index in range(len(s)):
            # if we are currently at the last of the s or current character is a space
            if s[str_index] == ' ' or str_index == len(s) - 1:
                first_character = last_space_index + 1
                last_character = str_index - 1 if s[str_index] == ' ' else str_index
                # swap first and last character
                while last_character > first_character:
                    s[first_character], s[last_character] = s[last_character], s[first_character]
                    first_character += 1
                    last_character -= 1
                # remember last_space_index for next iteration
                last_space_index = str_index
        return ''.join(s)
