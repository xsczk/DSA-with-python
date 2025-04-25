"""You are given an integer array nums. Two players are playing a game with this array:
player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first.
Both players start the game with a score of 0. At each turn, the player takes one of the numbers
from either end of the array (i.e., nums[0] or nums[nums.length - 1])
which reduces the size of the array by 1. The player adds the chosen number to their score.
The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal,
then player 1 is still the winner, and you should also return true.
You may assume that both players are playing optimally."""


class Solution:
    """
       [3,2,4]
        3/\4---------- 1st player's decision
     [2,4] [3,2]
     2/ \4  3/ \2----- 2nd player's decision
    [4][2] [2][3]
    """

    # Minimax Algorithm based on backtracking with memoization
    def predict_the_winner(self, nums: list[int]) -> bool:
        n = len(nums)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def minimax_algo(i, j):
            # base case:
            if i == j:
                return nums[i]
            if i > j:
                return 0
            if memo[i][j] != -1: return memo[i][j]
            # the min() function: since the opponent plays optimally,
            # they'll choose whichever option minimizes what the current player can get on their next turn
            left = nums[i] + min(
                # opponent picks nums[i+1] → current player's next turn starts at i+2
                minimax_algo(i + 2, j),
                # opponent picks nums[j] → current player's next turn is from i+1 to j-1
                minimax_algo(i + 1, j - 1),
            )
            right = nums[j] + min(
                minimax_algo(i + 1, j - 1),
                minimax_algo(i, j - 2),
            )
            # since the current player plays optimally, return max of option left or right
            memo[i][j] = max(left, right)
            return memo[i][j]

        player_1_score = minimax_algo(i=0, j=len(nums) - 1)
        player_2_score = sum(nums) - player_1_score
        return player_1_score >= player_2_score


solution = Solution()
is_player_1_won = solution.predict_the_winner([1, 5, 233, 7])
print(is_player_1_won)
