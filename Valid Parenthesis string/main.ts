/**
 * Given a string s containing only three types of characters: '(', ')' and '*',
 * return true if s is valid.
 *
 * The following rules define a valid string:
 *
 * Any left parenthesis '(' must have a corresponding right parenthesis ')'.
 * Any right parenthesis ')' must have a corresponding left parenthesis '('.
 * Left parenthesis '(' must go before the corresponding right parenthesis ')'.
 * '*' could be treated as a single right parenthesis ')' or a single left parenthesis '('
 * or an empty string "".
 *
 * Example 1:
 * Input: s = "()"
 * Output: true
 *
 * Example 2:
 * Input: s = "(*)"
 * Output: true
 *
 * Example 3:
 * Input: s = "(*))"
 * Output: true
 *
 * Constraints:
 * - 1 <= s.length <= 100
 * - s[i] is '(', ')' or '*'.
 */

function checkValidString(s: string): boolean {
    const openBrackets = []
    const asterisk = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(') openBrackets.push(i)
        else if (s[i] == '*') asterisk.push(i)
        else {
            if (openBrackets.length) openBrackets.pop()
            /** treat * as ( */
            else if (asterisk.length) asterisk.pop()
            else return false
        }
    }
    /** treat * as ) if openBrackets still doesn't empty */
    while (openBrackets.length && asterisk.length) {
        if (openBrackets.pop()! > asterisk.pop()!) return false
    }
    return !openBrackets.length
}