"""You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API."""


# Time complexity: O(log n)
# Space complexity: O(1)
class Solution:
    def is_bad_version(self, v):
        return v >= 2

    def first_bad_version(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if self.is_bad_version(mid):
                if mid == 1 or (mid - 1 > 0 and not self.is_bad_version(mid - 1)): return mid
                r = mid
            else:
                l = mid + 1
        return l


solution = Solution()
result = solution.first_bad_version(1)
print(result)
