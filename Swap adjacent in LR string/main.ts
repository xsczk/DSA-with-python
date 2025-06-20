/**
 * In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
 * a move consists of either replacing one occurrence of "XL" with "LX",
 * or replacing one occurrence of "RX" with "XR".
 * Given the starting string start and the ending string result,
 * return True if and only if there exists a sequence of moves to transform start to result.
 *
 * Constraints:
 * - 1 <= start.length <= 10^4
 * - start.length == result.length
 * - Both start and result will only consist of characters in 'L', 'R', and 'X'.
 */

function canTransform(start: string, result: string): boolean {
   // The frequency of 'X', 'R', and 'L' should be the same
   // in both the start and result strings
   let i = 0, j = 0
   const n = start.length
   while (i < n && j < n) {
      while (i < n && start[i] == 'X') {
         i++
      }
      while (j < n && result[j] == 'X') {
         j++
      }
      if (i < n && j < n) {
         if (start[i] != result[j] ||
             (start[i] == 'L' && i < j) ||
             (start[i] == 'R' && i > j)) {
            return false
         }
         i++
         j++
      }
   }
   while (i < n) {
      if (start[i] != 'X') return false
      i++
   }
   while (j < n) {
      if (result[j] != 'X') return false
      j++
   }
   return true
}