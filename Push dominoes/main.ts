/**
 * There are n dominoes in a line, and we place each domino vertically upright.
 * In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
 *
 * After each second, each domino that is falling to the left pushes the adjacent domino on the left.
 * Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
 *
 * When a vertical domino has dominoes falling on it from both sides,
 * it stays still due to the balance of the forces. (*)
 *
 * For the purposes of this question, we will consider that
 * a falling domino expends no additional force to a falling or already fallen domino.
 *
 * You are given a string dominoes representing the initial state where:
 *
 * - dominoes[i] = 'L', if the ith domino has been pushed to the left,
 * - dominoes[i] = 'R', if the ith domino has been pushed to the right, and
 * - dominoes[i] = '.', if the ith domino has not been pushed.
 * Return a string representing the final state.
 *
 * Constraints:
 * - n == dominoes.length
 * - 1 <= n <= 10^5
 * - dominoes[i] is either 'L', 'R', or '.'.
 */

// two pointers, string
// time complexity: O(n)
// space complexity: O(n)
function pushDominoes(dominoes: string): string {
   const n = dominoes.length
   const ans = dominoes.split('')
   let symbols: [number, string][] = dominoes.split('').map((c, i) => {
      if (c != '.') {
         return [i, c]
      }
   }).filter(Boolean) as typeof symbols
   symbols = [[-1, 'L'], ...symbols, [n, 'R']]
   for (let index = 1; index < symbols.length; index++) {
      const [i, x] = symbols[index - 1]
      const [j, y] = symbols[index]
      // R...R or L...L => replace "." with R or L
      if (x == y) {
         for (let k = i + 1; k < j; k++) ans[k] = x
      } else if (x == 'R' && y == 'L') { // R...L
         let l = i + 1, r = j - 1
         while (l < r) {
            ans[l] = x
            ans[r] = y
            l += 1
            r -= 1
         }
      }
   }
   return ans.join('')
}

console.log(pushDominoes(".L.R...LR..L.."))