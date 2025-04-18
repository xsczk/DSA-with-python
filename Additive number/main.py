"""An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence
must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros,
so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true
Explanation:
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
"""


class Solution:
    def is_additive_number(self, num: str) -> bool:
        def dfs(s: str, path: list[int]) -> bool:
            # base case: s is empty
            if not s:
                # if path is already had 3 or more items
                # that means it had a valid sequence
                return len(path) >= 3
            for i in range(1, len(s) + 1):
                if not self.is_valid(s[:i], path):
                    continue
                # continue checking for more valid sequence
                # if all recursive result are true => we know this num is met the requirement
                if dfs(s[i:], path + [int(s[:i])]): return True
            return False

        return dfs(s=num, path=[])

    def is_valid(self, s: str, path: list[int]):
        # make sure the input s doesn't contain leading zero
        if len(s) > 1 and s[0] == '0': return False
        # consider as valid if path len is smaller than 2 or
        # sum of the last two items is equal to s
        return len(path) < 2 or path[-1] + path[-2] == int(s)


solution = Solution()
is_additive = solution.is_additive_number('1203')
print(is_additive)
