"""Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4       1               4th row

"""
from collections import defaultdict


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def get_row(self, row_index: int) -> list[int]:
        ans = []
        memo = defaultdict(int)

        def get_val(row: int, col: int):
            # return directly if we found (row, col) in memo
            # to avoid re-calculate the same values over and over
            if (row, col) in memo: return memo[(row, col)]
            # base case: edges are always 1
            if col == 0 or row == col:
                memo[(row, col)] = 1
            else:
                memo[(row, col)] = get_val(row - 1, col - 1) + get_val(row - 1, col)
            return memo[(row, col)]

        for col in range(row_index + 1):
            ans.append(get_val(row=row_index, col=col))
        return ans


solution = Solution()
row = solution.get_row(row_index=4)
print(row)
# expected result: [1, 4, 6, 4, 1]
