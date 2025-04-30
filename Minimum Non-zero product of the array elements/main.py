"""You are given a positive integer p. Consider an array nums (1-indexed)
that consists of the integers in the inclusive range [1, 2^p - 1] in their binary representations.
You are allowed to do the following operation any number of times:

Choose two elements x and y from nums.
Choose a bit in x and swap it with its corresponding bit in y.
Corresponding bit refers to the bit that is in the same position in the other integer.
For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the right,
we have x = 1111 and y = 0001.

Find the minimum non-zero product of nums after performing the above operation any number of times.
Return this product modulo 10^9 + 7.

Note: The answer should be the minimum product before the modulo operation is done."""


class Solution:
    """
    initial       first        second
    1 = 001        001          001
    2 = 010        110          110
    3 = 011        001          001

    4 = 100        100          110
    5 = 101        001          001
    6 = 110        110          110

    7 = 111        111          111

    => there will be 2^(p - 1) // 2 number 1 and number 2^(p - 1) - 1
    min product of non-zero = (1 * 1 * 1 * ..). * (2^(p - 1) - 1 * 2^(p - 1) - 1) * ... * 2^(p - 1)
    """
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def min_non_zero_product(self, p: int) -> int:
        mod = 10 ** 9 + 7
        maximum = 2 ** p - 1
        num_of_representing = maximum // 2
        return pow(base=maximum - 1, exp=num_of_representing, mod=mod) * maximum % mod

solution = Solution()
min_product = solution.min_non_zero_product(3)
print(min_product)