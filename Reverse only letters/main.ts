/**
 * Given a string s, reverse the string according to the following rules:
 *
 * - All the characters that are not English letters remain in the same position.
 * - All the English letters (lowercase or uppercase) should be reversed.
 * Return s after reversing it.
 *
 * Constraints:
 * - 1 <= s.length <= 100
 * - s consists of characters with ASCII values in the range [33, 122].
 * - s does not contain '\"' or '\\'.
 */

// using two pointers
function reverseOnlyLetters(s: string): string {
   function isAlpha(s: string) {
      const charCode = s.charCodeAt(0)
      return (charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122);
   }
   const n = s.length
   const arr = s.split('')
   let l = 0, r = n - 1
   while (l < r) {
      while (l < r && !isAlpha(arr[l])) l++
      while (l < r && !isAlpha(arr[r])) r--
      const temp = arr[l]
      arr[l] = arr[r]
      arr[r] = temp
      l++
      r--
   }
   return arr.join('')
}

// using stack
function reverseOnlyLetters2(s: string): string {
    function isAlpha(s: string) {
        const charCode = s.charCodeAt(0)
        return (charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122);
    }
    const letters = []
    const ans = []
    for (const c of s) {
        isAlpha(c) && letters.push(c)
    }
    for (const c of s) {
        if (isAlpha(c)) {
            ans.push(letters.pop())
        } else {
            ans.push(c)
        }
    }
    return ans.join('')
};

console.log(reverseOnlyLetters("Test1ng-Leet=code-Q!"))