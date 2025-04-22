"""Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x."""

class Solution:
    def is_power_of_three(self, n: int) -> bool:
        """a number is power of three if n is divisible by 3 repeatedly until it equals to 1,
        if it cannot be reduced to 1, that means n is not a power of three
        """
        if n < 1: return False
        while n % 3 == 0:
            n /= 3
        return n == 1

solution = Solution()
ans = solution.is_power_of_three(45)
print(ans)