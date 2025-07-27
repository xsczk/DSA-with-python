"""
You start with an initial power of power, an initial score of 0,
and a bag of tokens given as an integer array tokens,
where each tokens[i] denotes the value of token-i.

Your goal is to maximize the total score by strategically playing these tokens.
In one move, you can play an unplayed token in one of the two ways
(but not both for the same token):

- Face-up: If your current power is at least tokens[i], you may play token-i,
losing tokens[i] power and gaining 1 score.
- Face-down: If your current score is at least 1, you may play token-i,
gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.

Constraints:
- 0 <= tokens.length <= 1000
- 0 <= tokens[i], power < 10^4
"""


class Solution:
    # greedy, two pointers, simulation
    # time complexity: O(n log n)
    # space complexity: O(n) due to sorting tokens
    def bag_of_tokens_score(self, tokens: list[int], power: int) -> int:
        low, high = 0, len(tokens) - 1
        score = 0
        tokens.sort()

        while low <= high:
            # play lowest tokens face-up when have enough power
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
            # we dont have enough power to play face-up
            # if we have enough score, we should play highest face-down
            # but only play if we have at least one token remaining after playing
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                return score
        return score
