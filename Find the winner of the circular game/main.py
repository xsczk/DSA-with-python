"""There are n friends that are playing a game. The friends are sitting in a circle
and are numbered from 1 to n in clockwise order.
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend
for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction including the friend you started at.
The counting wraps around the circle and may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle,
go back to step 2 starting from the friend immediately clockwise of the friend
who just lost and repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

"""
from collections import deque


class Solution:
    # simulation with queue
    # Time complexity: O(n * k)
    # Space complexity: O(n)
    def find_the_winner(self, n: int, k: int) -> int:
        step = k % n if k != n else k
        players = deque(range(1, n + 1))
        while len(players) > 1:
            for _ in range(step):
                lose = players.popleft()
                players.append(lose)
            players.pop()
        return players[0]

    # recursion
    # Time complexity: O(n)
    # Space complexity: O(n) recursion stack
    """
            0, 1, 2, 3, 4  first round
    index:  0, 1, 2, 3, 4
    
            0, 2, 3, 4     second round
    index:  3, 0, 1, 2
    
            0, 2, 4        third round
    index:  1, 2, 0
    
            2, 4           forth round
    index:  0, 1
    
            2              winner
    index:  0
    """

    def find_the_winner_2(self, n: int, k: int) -> int:
        def find_winner(n: int, k: int) -> int:
            """function that returns the index of the winning friend
            with a game of n friends and a step size of k. """
            if n == 1: return 0
            return (find_winner(n - 1, k) + k) % n

        # add 1 to convert back to 1 indexing
        return find_winner(n, k) + 1


solution = Solution()
winner = solution.find_the_winner_2(5, 2)
print(winner)
