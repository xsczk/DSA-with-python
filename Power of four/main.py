"""Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

"""


class Solution:
    # iterative: the ideal is the same as power of three's problem
    # Time complexity: O(log n)
    # Space complexity: 0(1)
    def is_power_of_four(self, n: int) -> bool:
        if n < 1: return False
        while n % 4 == 0:
            n /= 4
        return n == 1

    # bit manipulation
    # Time complexity: O(1)
    # Space complexity: O(1)
    def is_power_of_four_2(self, n: int) -> bool:
        """we know that the power of four is also the power of two.
        So first, check that n has only one bit set.
        But not all powers of 2 are powers of 4. For powers of 4, n - 4 must be divisible by 3"""
        return n > 0 and n & (n - 1) == 0 and (n - 4) % 3 == 0

solution = Solution()
ans = solution.is_power_of_four(64)
print(ans)