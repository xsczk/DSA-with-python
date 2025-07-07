/**
 * Given two strings s and t, return true if they are equal when both are typed
 * into empty text editors. '#' means a backspace character.
 *
 * Note that after backspacing an empty text, the text will continue empty.
 *
 * Constraints:
 * - 1 <= s.length, t.length <= 200
 * - s and t only contain lowercase letters and '#' characters.
 */

// based on the second python approach using generator function
function backspaceCompare(s: string, t: string): boolean {
   function* generator(S: string): Generator<string> {
      let skip = 0
      for (let i = S.length - 1; i >= 0; i--) {
         const c = S[i]
         if (c == '#') {
            skip++
         } else if (skip) {
            skip--
         } else yield c
      }
   }

   const genS = generator(s), genT = generator(t)
   while (true) {
      const objS = genS.next(), objT = genT.next()
      if (objS.done && objT.done) {
         return true
      }
      if (objS.value != objT.value) {
         return false
      }
   }
}

console.log(backspaceCompare("ab#c", "ad#c"))