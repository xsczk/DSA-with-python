/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 *
 * An input string is valid if:
 *
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 *
 * Constraints:
 * - 1 <= s.length <= 10^4
 * - s consists of parentheses only '()[]{}'.
 */

function isValid(s: string): boolean {
   const stack = []
   const map = {
      '[': ']',
      '(': ')',
      '{': '}'
   }
   for (const bracket of s) {
      if (map[bracket]) {
         stack.push(bracket)
      } else {
         if (!stack.length) return false
         const open = stack.pop()
         if (map[open] != bracket) {
            return false
         }
      }
   }
   return !stack.length
}

console.log(isValid("[{}([])[]({{}})]"))