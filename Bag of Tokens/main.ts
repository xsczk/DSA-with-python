/**
 * You start with an initial power of power, an initial score of 0,
 * and a bag of tokens given as an integer array tokens,
 * where each tokens[i] denotes the value of token-i.
 *
 * Your goal is to maximize the total score by strategically playing these tokens.
 * In one move, you can play an unplayed token in one of the two ways
 * (but not both for the same token):
 *
 * - Face-up: If your current power is at least tokens[i], you may play token-i,
 * losing tokens[i] power and gaining 1 score.
 * - Face-down: If your current score is at least 1, you may play token-i,
 * gaining tokens[i] power and losing 1 score.
 * Return the maximum possible score you can achieve after playing any number of tokens.
 *
 * Constraints:
 * - 0 <= tokens.length <= 1000
 * - 0 <= tokens[i], power < 10^4
 */

function bagOfTokensScore(tokens: number[], power: number): number {
   let low = 0, high = tokens.length - 1
   let score = 0
   tokens.sort((a, b) => a - b)
   while (low <= high) {
      if (power >= tokens[low]) {
         score += 1
         power -= tokens[low]
         low += 1
      } else if (low < high && score > 0) {
         score -= 1
         power += tokens[high]
         high -= 1
      } else return score
   }
   return score
}