/**
 * Given a positive integer n, find the smallest integer which has exactly the same digits existing
 * in the integer n and is greater in value than n. If no such positive integer exists, return -1.
 *
 * Note that the returned integer should fit in 32-bit integer, if there is a valid answer,
 * but it does not fit in 32-bit integer, return -1.
 *
 * Constraints:
 * - 1 <= n <= 2^31 - 1
 */

function nextGreaterElement(n: number): number {
   let strNum = String(n).split('')
   const lastIndex = strNum.length - 1
   let i = lastIndex
   let j = i
   // find the first decreasing element from the right
   while (i - 1 >= 0 && strNum[i] <= strNum[i - 1]) {
      i--
   }
   // it i at index 0, there is no valid answer
   if (!i) return -1
   const lastCharIndex = i - 1
   // reverse the remaining s start from index i
   while (i < j) {
      [strNum[i], strNum[j]] = [strNum[j], strNum[i]]
      i++
      j--
   }
   i = lastIndex
   while (i > 0 && strNum[i] > strNum[lastCharIndex]) {
      i--
   }
   // swap the num at last_char_index with the num at index i + 1
   [strNum[lastCharIndex], strNum[i + 1]] = [
      strNum[i + 1], strNum[lastCharIndex]
   ]
   let res = 0
   // convert strNum to number
   for (let i = 0; i < strNum.length; i++) {
      res += Number(strNum[i]) * 10 ** (lastIndex - i)
   }
   if (res <= 2 ** 31 - 1) {
      return res
   }
   return -1
}

console.log(nextGreaterElement(234157641))