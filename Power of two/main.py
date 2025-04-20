"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""


class Solution:
    # bit manipulation - math
    # Time complexity: O(1)
    # Space complexity: O(1)
    def is_power_of_two(self, n: int) -> bool:
        """Any power of two has exactly one bit set in its binary representation.
        For example, 8 is 1000 and 16 is 10000. If you subtract 1 from such numbers,
        all bits to the right of the set bit become 1, and a bitwise AND will result in zero.
        Ex: 16 (10000) - 1 (00001) = 15 (01111) then 10000 AND 01111 == 0
        """
        return n > 0 and (n & n - 1) == 0

    # iterative
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def is_power_of_two_2(self, n: int) -> bool:
        """
        Example of the solution:
            16 ÷ 2 = 8, remainder = 0
            8 ÷ 2 = 4, remainder = 0
            4 ÷ 2 = 2, remainder = 0
            2 ÷ 2 = 1, remainder = 0
            1 ÷ 2 = 0, remainder = 1
        """
        cnt = 0
        while n > 0:
            if n % 2 == 1: cnt += 1
            n //= 2
        # the power of two's number only has exactly one bit 1 in binary form
        # 16 (10000); 8 (1000)
        return cnt == 1

    # recursion based on the iterative approach
    # Time complexity: O(log n)
    # Space complexity: O(log n) due to recursion call stack
    def is_power_of_two_3(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        if n % 2 == 1: return False
        return self.is_power_of_two_3(n=n // 2)


solution = Solution()
ans = solution.is_power_of_two_3(32)
print(ans)
