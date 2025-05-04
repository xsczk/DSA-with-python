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

    # dynamic programing - refer https://www.geeksforgeeks.org/longest-palindromic-substring/
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def longest_palindrome_dp(self, s: str) -> str:
        n = len(s)
        # create dp table to store status of substring from i -> j if s[i...j]
        # is a palindrome or not
        dp = [[False] * n for _ in range(n)]
        # keep track the starting index and the current palindrome's max len
        start, max_len = 0, 1

        # all substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # all substrings of length 2 with same characters are also palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                # update the max_len if it smaller than 2
                if max_len < 2:
                    start = i
                    max_len = 2

        # check for lengths of the palindrome from 3 -> n
        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                # last index of current substring has len `length`
                j = i + length - 1
                # if the substring from i + 1 -> j - 1 is a palindrome and s[i] == s[j]
                # => the substring from i -> j is also a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    # update the max_len
                    if length > max_len:
                        max_len = length
                        start = i
        return s[start:start + max_len]


solution = Solution()
palindrome = solution.longest_palindrome_dp("babaddtattarrattatddetartrateedredividerb")
print(palindrome)
