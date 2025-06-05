"""Given a non-negative integer c, decide whether there're two integers a and b
such that a2 + b2 = c."""
import math


class Solution:
    def judge_square_sum(self, c: int) -> bool:
        a, b = 0, round(math.sqrt(c))
        while a < b:
            square_sum = a * a + b * b
            if square_sum == c:
                return True
            elif square_sum < c:
                a += 1
            else:
                b -= 1
        return False
