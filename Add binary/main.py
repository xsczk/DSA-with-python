"""Given two binary strings a and b, return their sum as a binary string."""

# Time complexity: O(n) - n is the length of either a or b, whichever is longer.
# Space complexity: O(n) - the result str
class Solution:
    def add_binary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            result = f'{carry % 2}{result}'
            carry //= 2
        return result

solution = Solution()
binary_sum = solution.add_binary(a='1011', b='1101')
print(binary_sum)