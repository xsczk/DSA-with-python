"""There is a regular convex polygon with n vertices.
The vertices are labeled from 0 to n - 1 in a clockwise direction,
and each vertex has exactly one monkey.


Simultaneously, each monkey moves to a neighboring vertex.
A collision happens if at least two monkeys reside on the same vertex after the movement
or intersect on an edge.

Return the number of ways the monkeys can move so that at least one collision happens.
Since the answer may be very large, return it modulo 10^9 + 7."""

class Solution:
    def monkey_move(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # total possible moves of all the monkey is 2^n where n is the number of monkey
        # there are 2 invalid cases where all the monkey move but no collision happens
        # (all move in clockwise direction or in anticlockwise direction)
        # => the answer will be:
        return (pow(2, n, mod) - 2) % mod

solution = Solution()
num_of_ways = solution.monkey_move(4)
print(num_of_ways)
