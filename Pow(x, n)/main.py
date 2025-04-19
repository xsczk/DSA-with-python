"""Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)."""


class Solution:
    # recursion
    # Time complexity: O(log n)
    # Space complexity: O(log n) due to recursion call stack
    def my_pow(self, x: float, n: int) -> float:
        # base case: any number raised to 0 is 1
        if n == 0: return 1.0

        # if n < 0, x^n == 1 / (x^-n)
        if n < 0: return 1 / self.my_pow(x, -n)

        # if n is even: x^n = (x^(n//2))^2 and x^n = x * (x^(n//2))^2 otherwise
        half = self.my_pow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x

    # iterative approach based on recursion approach above
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def my_pow_2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        while n > 0:
            # if the current bit is 1, multiplies result by x
            # we can check current bit is 1 or not by checking if n is even or odd number
            # ex: 9 -> 1001 -> 2^3 + 2^2 (skip) + 2^1 (skip) + 2^0
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result



solution = Solution()
pow = solution.my_pow_2(x=2.00000, n=5)
print(pow)