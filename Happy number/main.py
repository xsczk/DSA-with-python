"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not."""


class Solution:
    # hash table to store visited value
    # Time complexity: O(log n) due to get_next method, operates log n times with each digit
    # Space complexity: O(k) for storing k numbers in the set
    def is_happy(self, n: int) -> bool:
        visited = set()

        # get next value by calc sum of the squares of n's digit
        def get_next(n: int) -> int:
            ans = 0
            while n > 0:
                digit = n % 10
                ans += digit * digit
                n //= 10
            return ans

        # loop until n == 1 or n has already in visited.
        # if n = 1 => n is a happy number, otherwise if n has already seen in visited, which means
        # it will cause infinite loop => return False
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next(n)
        return n == 1

    # Floyd's cycle detection, mathematics
    # Time complexity: O(n)
    # Space complexity: O(1)
    def is_happy_2(self, n: int) -> bool:
        # get next value by calc sum of the squares of n's digit
        def get_next(n: int) -> int:
            ans = 0
            while n > 0:
                digit = n % 10
                ans += digit * digit
                n //= 10
            return ans

        # instead of using set to store visited number in each interation,
        # we simply use slow and fast pointer to detect if there is a cycle aka infinite loop
        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1



solution = Solution()
ans = solution.is_happy_2(19)
print(ans)
