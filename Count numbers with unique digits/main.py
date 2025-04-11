"""Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

"""


class Solution:
    # using combinatorics in math
    def count_numbers_with_unique_digits(self, n: int) -> int:
        if n == 0: return 1

        def count_unique_digits(x: int):
            if x == 1: return 10
            possible_digits = 9
            # except for first digits, we have 9 choices
            # since a number cannot start with 0
            # from the second digits, we have 11-x choices where x is the digit position
            for i in range(1, x):
                # we have 9 * 9 * 8 numbers with unique 3 digits
                possible_digits *= 10 - i
            return possible_digits

        cnt = 0
        for digits in range(1, n + 1):
            cnt += count_unique_digits(digits)
        return cnt