/**
 * Given a string s, return true if the s can be palindrome
 * after deleting at most one character from it.
 *
 * Constraints:
 * - 1 <= s.length <= 10^5
 * - s consists of lowercase English letters.
 */

function validPalindrome(s: string): boolean {
   let left = 0, right = s.length - 1

   function isPalindrome(i: number, j: number): boolean {
      while (i < j) {
         if (s[i] != s[j]) return false
         i++
         j--
      }
      return true
   }

   while (left < right) {
      if (s[left] != s[right]) {
         return isPalindrome(left + 1, right) || isPalindrome(left, right - 1)
      }
      left++
      right--
   }
   return true
}

function validPalindrome2(s: string): boolean {
   let left = 0, right = s.length - 1
   while (left < right) {
      if (s[left] != s[right]) {
         const skipLeft = s.slice(left + 1, right + 1),
             skipRight = s.slice(left, right)
         return skipLeft == skipLeft.split('').reverse()
                 .join('') ||
             skipRight == skipRight.split('').reverse().join('')
      }
      left++
      right--
   }
   return true
}