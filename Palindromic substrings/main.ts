/**
 * Given a string s, return the number of palindromic substrings in it.
 *
 * A string is a palindrome when it reads the same backward as forward.
 *
 * A substring is a contiguous sequence of characters within the string.
 *
 * Constraints:
 * - 1 <= s.length <= 1000
 * - s consists of lowercase English letters.
 */

// dynamic programing, memoization
// time complexity: O(n^2)
// space complexity: O(n^2) due to 2D-dp list
function countSubstrings(s: string): number {
   let ans = 0
   if (!s) return ans
   const n = s.length
   const dp = Array.from({length: n}, () => Array(n).fill(false))
   // every single character is a palindrome
   for (let i = 0; i < n; i++) {
      dp[i][i] = true
      ans++
   }
   // check for substrings that have length >= 2
   for (let length = 2; length <= n; length++) {
      for (let start = 0; start <= n - length; start++) {
         const end = start + length - 1
         // if abc is a palindrome and x = y => xabcy is also a palindrome
         if (s[start] == s[end] && (length == 2 || dp[start + 1][end - 1])) {
            dp[start][end] = true
            ans++
         }
      }
   }
   return ans
}

// two pointers, expand to determine if the next substring is a palindrome
// time complexity: O(n^2)
// space complexity: O(1)
function countSubstrings2(s: string): number {
   let ans = 0
   if (!s) return ans

   function expand(i: number, j: number): number {
      let l = i, r = j, numOfPalindrome = 0
      while (l >= 0 && r < s.length && s[l] == s[r]) {
         l--
         r++
         numOfPalindrome += 1
      }
      return numOfPalindrome
   }

   for (let i = 0; i < s.length; i++) {
      ans += expand(i, i) + expand(i, i + 1)
   }
   return ans
}

countSubstrings('abc')