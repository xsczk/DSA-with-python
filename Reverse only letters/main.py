"""
Given a string s, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '\"' or '\\'.
"""

class Solution:
    # two pointers, reverse only alphabetic characters
    def reverse_only_letters(self, s: str) -> str:
        n = len(s)
        s = list(s)
        l, r = 0, n - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while r > l and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

    # stack
    def reverse_only_letter_2(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)