"""You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make
using the letters printed on those tiles."""
from collections import Counter


class Solution:
    def num_tile_possibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        count = [0]

        def backtrack(i):
            for k, v in freq.items():
                if v != 0:
                    freq[k] -= 1
                    count[0] += 1
                    backtrack(i+1)
                    freq[k] += 1
            return count[0]

        return backtrack(0)

solution = Solution()
ans = solution.num_tile_possibilities('AAB')
print(ans)