/**
 * Given a string s and a character c that occurs in s,
 * return an array of integers answer where answer.length == s.length
 * and answer[i] is the distance from index i to the closest occurrence of character c in s.
 *
 * The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
 *
 * Constraints:
 * - 1 <= s.length <= 10^4
 * - s[i] and c are lowercase English letters.
 * - It is guaranteed that c occurs at least once in s.
 */
import {eachRight} from 'lodash'

// traverse twice
function shortestToChar(s: string, c: string): number[] {
   const n = s.length
   const ans = Array.from({length: n}, () => 0)
   let prev = -Infinity
   s.split('').forEach((char, i) => {
      if (char == c) {
         prev = i
      }
      ans[i] = i - prev
   })
   prev = Infinity
   eachRight(s, (char, i) => {
      if (char == c) {
         prev = i
      }
      ans[i] = Math.min(ans[i], prev - i)
   })
   return ans
}

// update the ans[i] one by one
// time complexity: O(n)
// space complexity: O(n)
function shortestToChar2(s: string, c: string): number[] {
   const ans = Array.from({length: s.length}, () => 0)
   const cIndexes = [], arr = s.split('')
   arr.forEach((char, i) => {
      if (char == c) cIndexes.push(i)
   })
   let prevIndex = Infinity
   arr.forEach((char, i) => {
      ans[i] = Math.min(Math.abs(prevIndex - i), Math.abs(cIndexes[0] - i))
      if (cIndexes.length > 1 && c == char) {
         prevIndex = cIndexes.shift()
      }
   })
   return ans
}