/**
 * Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
 * the key might get long pressed, and the character will be typed 1 or more times.
 *
 * You examine the typed characters of the keyboard. Return True if it is possible that
 * it was your friends name, with some characters (possibly none) being long pressed.
 *
 * Constraints:
 * - 1 <= name.length, typed.length <= 1000
 * - name and typed consist of only lowercase English letters.
 */

function isLongPressedName(name: string, typed: string): boolean {
   let np = 0, tp = 0
   while (np < name.length && tp < typed.length) {
      if (name[np] == typed[tp]) {
         np++
         tp++
      } else if (tp >= 1 && typed[tp] == typed[tp - 1]) {
         tp++
      } else return false
   }
   // name = "alexd"  typed = "ale"
   if (np != name.length) {
      return false
   }
   while (tp < typed.length) {
      if (typed[tp] != typed[tp - 1]) {
         return false
      }
      tp++
   }
   return true
}

console.log(isLongPressedName('alex', 'aaleexa'))