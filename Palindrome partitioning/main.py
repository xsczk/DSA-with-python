"""Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Note:
- A palindrome is a string that reads the same forward and backward.
- A substring is a contiguous non-empty sequence of characters within a string.
"""

"""
    'aab'
    / | \
  a   aa aab
 / \  |
a  ab b
|
b

[[a, a, b], [aa, b]]
"""
# Time complexity: O(2^n)
# Space complexity: O(n)
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        par = []

        def backtrack(s: str):
            # when s is empty and len of partition list > 0
            # that means we have found a valid partition
            if len(s) == 0 and len(par) > 0:
                ans.append(par[:])
                return
            for i in range(1, len(s) + 1):
                sub_str = s[0:i]
                if self.is_palindrome(sub_str):
                    par.append(sub_str)
                    backtrack(s=s[i:])
                    par.pop()
            return

        backtrack(s=s)
        return ans

    def is_palindrome(self, s: str) -> bool:
        # return s == s[::-1]
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True


solution = Solution()
ans = solution.partition(s='aab')
print(ans)