"""A digit string is good if the digits (0-indexed) at even indices are even
and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even
and the digits (5 and 2) at odd positions are prime.
However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n.
Since the answer may be large, return it modulo 10^9 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros."""


class Solution:
    # math with exponentiation
    # Time complexity: O(log n)
    # explanation: each digit at even indices can be one of the 5 even digits (0, 2, 4, 6, 8)
    # and can be one of (2, 3, 5, 7) if they are at odd indices.
    # => as we know about combinatorics, if n is even,
    # the total number of good numbers is 5^(n/2) * 4^(n/2).
    # if n is odd, the total number of good numbers is 5^(n+1)/2) * 4^(n/2).
    def count_good_numbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # refer pow(x, n) sub problem
        # 9 (1001) = 2^3 + 2^0 => x^9 = x^(2^3) * x^(2^0) = x^8 * x
        # use fast exponentiation to calculate x^y % mod
        def pow(x: int, y: int) -> float:
            res = 1
            while y > 0:
                if y % 2 != 0:
                    res = res * x % mod
                x = x * x % mod
                y //= 2
            return res

        return pow(x=5, y=((n + 1) // 2)) * pow(x=4, y=n // 2) % mod


solution = Solution()
good_numbers = solution.count_good_numbers(806166225460393)
print(good_numbers)
