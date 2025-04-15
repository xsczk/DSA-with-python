"""In a gold mine grid of size m x n,
each cell in this mine has an integer representing the amount of gold in that cell,
0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold."""


class Solution:
    def get_maximum_gold(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        # possible path
        DIRECTIONS = [-1, 0, 1, 0, -1]

        def find_max(i: int, j: int) -> int:
            # base case: this cell is not in the matrix or has no gold
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == 0: return 0
            max_gold = 0
            gold = grid[i][j]
            # mark as visited
            grid[i][j] = 0
            # 4 directions possible: up, down, left, right
            for direction in range(4):
                # find max in every possible directions
                max_gold = max(max_gold, find_max(i=DIRECTIONS[direction] + i,
                                                  j=DIRECTIONS[direction + 1] + j))
            # backtrack
            grid[i][j] = gold
            return max_gold + gold

        for i in range(rows):
            for j in range(cols):
                # find max in every possible paths
                ans = max(ans, find_max(i, j))
        return ans


solution = Solution()
ans = solution.get_maximum_gold(grid=[[0, 6, 0],
                                      [5, 8, 7],
                                      [0, 9, 0]])

print(ans)
