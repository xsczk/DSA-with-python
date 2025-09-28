/**
 * Given string num representing a non-negative integer num, and an integer k,
 * return the smallest possible integer after removing k digits from num.
 *
 * Example 1:
 * - Input: num = "1432219", k = 3
 * - Output: "1219"
 * - Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
 * which is the smallest.
 *
 * Example 2:
 * - Input: num = "10200", k = 1
 * - Output: "200"
 * - Explanation: Remove the leading 1 and the number is 200.
 * Note that the output must not contain leading zeroes.
 *
 * Example 3:
 * - Input: num = "10", k = 2
 * - Output: "0"
 * - Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 *
 * Constraints:
 * - 1 <= k <= num.length <= 10^5
 * - num consists of only digits.
 * - num does not have any leading zeros except for the zero itself.
 */

function removeKdigits(num: string, k: number): string {
    const incSt: string[] = []
    let i = 0
    while (i < num.length && k > 0) {
       /** we can compare string here since the input contains only digits */
        while (incSt.length && (incSt.at(-1) ?? '') > num[i] && k > 0) {
            incSt.pop()
            k -= 1
        }
        incSt.push(num[i])
        i += 1
    }
    if (i < num.length) {
        incSt.push(num.slice(i))
    }
    while (incSt.length && k > 0) {
        incSt.pop()
        k -= 1
    }
    /** apply Regex to remove leading zeros (replace them with empty string) */
    return incSt.join('').replace(/^0+/, '') || "0"
};