"""Given a string s, return the longest palindromic substring in s."""


class Solution:
    # two pointer - expand from the middle to find the longest palindrome substring
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def longest_palindrome(self, s: str) -> str:
        if not s: return ''

        def expand(i: int, j: int) -> tuple[int, int]:
            l, r = i, j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # return the start and end of the palindrome
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(len(s)):
            # palindrome has odd len if we pass two param which have the same value
            # or even len if j - i = 1
            l1, r1 = expand(i, i)  # odd-length palindrome
            l2, r2 = expand(i, i + 1)  # even-length palindrome

            # investigate the longest palindrome substring
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]


solution = Solution()
palindrome = solution.longest_palindrome("babaddtattarrattatddetartrateedredividerb")
print(palindrome)
