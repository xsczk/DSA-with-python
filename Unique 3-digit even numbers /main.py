"""You are given an array of digits called digits.
Your task is to determine the number of distinct three-digit even numbers
that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros."""


class Solution:
    # brute-force nested loop
    # Time complexity: O(n^3)
    # Space complexity: O(min(n^3, 900)) ~ O(1)
    def total_numbers(self, digits: list[int]) -> int:
        nums = set()
        n = len(digits)
        for i in range(n):
            # num cannot start at 0
            if digits[i] == 0: continue
            for j in range(n):
                # skip duplicate
                if j == i: continue
                for k in range(n):
                    # skip duplicate and if last character is an odd number
                    if k == i or k == j or digits[k] % 2: continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(num)
        return len(nums)

    # backtracking
    # Time complexity: O(n^3)
    # Space complexity: O(n + k) - n is recursion call stack; k is len(res)
    def total_numbers_2(self, digits: list[int]) -> int:
        used = set()
        res = set()  # for 3-length digits

        def backtrack(cur):
            # base case: cur >= 100
            if cur // 100:
                # if cur is an even number, add cur to res
                if cur % 2 == 0:
                    res.add(cur)
                return
            for i, n in enumerate(digits):
                if i not in used:
                    used.add(i)
                    backtrack(cur * 10 + n)
                    used.remove(i)

        backtrack(0)
        return len(res)


solution = Solution()
total = solution.total_numbers_2([1, 2, 3, 4])
print(total)
