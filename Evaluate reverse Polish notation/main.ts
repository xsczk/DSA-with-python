/**
 * You are given an array of strings tokens that represents an arithmetic expression
 * in a Reverse Polish Notation.
 *
 * Evaluate the expression. Return an integer that represents the value of the expression.
 *
 * Note that:
 * - The valid operators are '+', '-', '*', and '/'.
 * - Each operand may be an integer or another expression.
 * - The division between two integers always truncates toward zero.
 * - There will not be any division by zero.
 * - The input represents a valid arithmetic expression in a reverse polish notation.
 * - The answer and all the intermediate calculations can be represented in a 32-bit integer.
 *
 * Constraints:
 * - 1 <= tokens.length <= 104
 * - tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
 */

function evalRPN(tokens: string[]): number {
   const stack: number[] = [];
   const expression = ['+', '-', '*', '/']
   for (const token of tokens) {
      if (expression.includes(token)) {
         const a = stack.pop() as number,
             b = stack.pop() as number;
         if (token == '+') {
            stack.push(b + a)
         } else if (token == '-') {
            stack.push(b - a)
         } else if (token == '*') {
            stack.push(b * a)
         } else {
            stack.push(Math.trunc(b / a))
         }
      } else {
         stack.push(Number(token))
      }
   }
   return stack[0]
};