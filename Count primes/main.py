"""Given an integer n, return the number of prime numbers
that are strictly less than n."""
import math


# Using Sieve of Eratosthenes
class Solution:
    def count_primes(self, n: int) -> int:
        primes = [True] * n
        p = 2
        count = 0
        while p ** 2 < n:
            if primes[p]:
                for i in range(p ** 2, n, p):
                    primes[i] = False
            p += 1
        """Start range from 2 because 0 and 1 aren't prime number"""
        for i in range(2, n):
            if primes[i]: count += 1
        return count


solution = Solution()
result = solution.count_primes(18)
print(result)