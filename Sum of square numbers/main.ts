/**
 * Given a non-negative integer c, decide whether there're two integers a and b
 * such that a2 + b2 = c.
 */

function judSquareSum(c: number): boolean {
   let a = 0, b = Math.round(Math.sqrt(c))
   while (a < b) {
      const squareSum = a * a + b * b
      if (squareSum == c) return true
      else if (squareSum < c) {
         a++
      } else {
         b--
      }
   }
   return false
}