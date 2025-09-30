/**
 * You are given two non-empty linked lists representing two non-negative integers.
 * The most significant digit comes first and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Example 1:
 * Input: l1 = [7,2,4,3], l2 = [5,6,4]
 * Output: [7,8,0,7]
 *
 * Example 2:
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [8,0,7]
 *
 * Example 3:
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 * Constraints:
 * - The number of nodes in each linked list is in the range [1, 100].
 * - 0 <= Node.val <= 9
 * - It is guaranteed that the list represents a number that does not have leading zeros.
 */

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    function addToStack(l: ListNode | null): number[] {
        const st: number[] = []
        while (l) {
            st.push(l.val)
            l = l.next
        }
        return st
    }
    const s1 = addToStack(l1)
    const s2 = addToStack(l2)
    let total = 0, carry = 0
    let res = new ListNode()
    while (s1.length || s2.length) {
        if (s1.length) {
            total += s1.pop()!
        }
        if (s2.length) {
            total += s2.pop()!
        }
        res.val = total % 10
        carry = Math.floor(total / 10)
        const head = new ListNode(carry)
        head.next = res
        res = head
        total = carry
    }
    return carry == 0 ? res.next : res
};