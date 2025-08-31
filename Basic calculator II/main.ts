/**
 * Given a string s which represents an expression, evaluate this expression and return its value.
 *
 * The integer division should truncate toward zero.
 *
 * You may assume that the given expression is always valid.
 * All intermediate results will be in the range of [-231, 231 - 1].
 *
 * Note: You are not allowed to use any built-in function which evaluates strings
 * as mathematical expressions, such as eval().
 *
 * Constraints:
 * - 1 <= s.length <= 3 * 10^5
 * - s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
 * - s represents a valid expression.
 * - All the integers in the expression are non-negative integers in the range [0, 231 - 1].
 * - The answer is guaranteed to fit in a 32-bit integer.
 */

function calculate(s: string): number {
   if (!s) {
      return 0;
   }
   const stack: number[] = []
   let currentNumber = 0, operation = '+'
   s = s.trim()
   for (let i = 0; i < s.length; i++) {
      const char = s[i]
      if (char === ' ') {
         continue
      }
      if ('0' <= char && char <= '9') {
         currentNumber = currentNumber * 10 + (char.charCodeAt(0) - '0'.charCodeAt(0))
      }
      if ('0' > char || char > '9' || i === s.length - 1) {
         if (operation === '+') {
            stack.push(currentNumber);
         } else if (operation === '-') {
            stack.push(-currentNumber);
         } else if (operation === '*') {
            const top = stack.pop() as number;
            stack.push(currentNumber * top)
         } else {
            const top = stack.pop() as number;
            stack.push(Math.trunc(top / currentNumber))
         }
         currentNumber = 0
         operation = char
      }
   }
   let result = 0
   while (stack.length) {
      result += stack.at(-1) as number
      stack.pop()
   }
   return result;
};