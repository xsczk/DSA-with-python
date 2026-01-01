/**
 * Given a balanced parentheses string s, return the score of the string.
 *
 * The score of a balanced parentheses string is based on the following rule:
 *
 * "()" has score 1.
 * AB has score A + B, where A and B are balanced parentheses strings.
 * (A) has score 2 * A, where A is a balanced parentheses string.
 *
 *
 * Example 1:
 * - Input: s = "()"
 * - Output: 1
 *
 * Example 2:
 * - Input: s = "(())"
 * - Output: 2
 *
 * Example 3:
 * - Input: s = "()()"
 * - Output: 2
 *
 * Constraints:
 * - 2 <= s.length <= 50
 * - s consists of only '(' and ')'.
 * - s is a balanced parentheses string.
 */

// array
// time complexity: O(n)
// space complexity: O(1)
function scoreOfParentheses(s: string): number {
   const res: number[] = Array(30).fill(0)
   let i = 0
   for (const c of s) {
      if (c == '(') {
         // initialize new scope
         res[++i] = 0
      } else {
         res[--i] += res[i + 1] + Math.max(res[i + 1], 1)
      }
   }
   return res[0]
}