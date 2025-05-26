"""Given a string s and an integer k, reverse the first k characters for every 2k characters
counting from the start of the string.

If there are fewer than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original."""

class Solution:
    # two pointers
    # Time complexity: O(n) - each character is visited once
    # Space complexity: O(n) - due to transforming word to list
    def reverse_str(self, s: str, k: int) -> str:
        # split every 2k characters counting from the start of s
        s = [s[i : i + 2 * k] for i in range(0, len(s), 2 * k)]

        def reverse_k_characters(s: list[str]) -> str:
            l, r = 0, len(s) - 1 if len(s) < k else k - 1
            while l < r:
                # swap left and right element
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            return ''.join(s)

        ans = ''
        for word in s:
            ans += reverse_k_characters(list(word))
        return ans