/**
 * Given a string containing just the characters '(' and ')', return the length
 * of the longest valid (well-formed) parentheses substring.
 * A substring is a contiguous non-empty sequence of characters within a string.
 *
 * Constraints:
 * - 0 <= s.length <= 3 * 10^4
 * - s[i] is '(', or ')'.
 */

import {isEmpty} from 'lodash'

function longestValidParentheses(s: string): number {
   let stack: number[] = []
   let last_invalid = -1
   let max_len = 0
   for (let i = 0; i < s.length; i++) {
      if (s[i] == '(') {
         stack.push(i)
      } else if (!isEmpty(stack)) {
         stack.pop()
         const start = !isEmpty(stack) ? (stack.at(-1) as number) + 1 : last_invalid + 1
         max_len = Math.max(max_len, i - start + 1)
      } else {
         stack = []
         last_invalid = i
      }
   }
   return max_len
}

console.log(longestValidParentheses(")()())"))
