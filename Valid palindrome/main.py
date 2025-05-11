"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        # turn s in to lower case
        s = s.lower()
        while l < r:
            # skip and increase l if s[l] is not alphanumeric character
            if not s[l].isalnum():
                l += 1
                continue
            # skip and decrease r if s[r] is not alphanumeric character
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        # if pass the while loop, that means the s is a valid palindrome
        return True

solution = Solution()
res = solution.is_palindrome('A man, a plan, a canal: Panama')
print(res)