/**
 * A permutation perm of n + 1 integers of all the integers in the range [0, n]
 * can be represented as a string s of length n where:
 *
 * - s[i] == 'I' if perm[i] < perm[i + 1], and
 * - s[i] == 'D' if perm[i] > perm[i + 1].
 * Given a string s, reconstruct the permutation perm and return it.
 * If there are multiple valid permutations perm, return any of them.
 *
 * Constraints:
 * - 1 <= s.length <= 10^5
 * - s[i] is either 'I' or 'D'.
 */

function diStringMatch(s: string): number[] {
    const ans = []
    let l = 0, r = s.length
    for (const c of s) {
        if (c == 'I') {
            ans.push(l)
            l++
        } else {
            ans.push(r)
            r--
        }
    }
    ans.push(r)
    return ans
}