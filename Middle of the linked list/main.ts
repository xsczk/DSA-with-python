/**
 * Given the head of a singly linked list, return the middle node of the linked list.
 *
 * If there are two middle nodes, return the second middle node.
 *
 * Constraints:
 * - The number of nodes in the list is in the range [1, 100].
 * - 1 <= Node.val <= 100
 */

/**
 * Definition for singly-linked list.
 */

class ListNode {
   val: number
   next: ListNode | null

   constructor(val = 0, next?: ListNode | null) {
      this.val = val
      this.next = (next === undefined ? null : next)
   }
}

function middleNode(head: ListNode | null): ListNode | null {
   let slow = head, fast = head
   while (fast && fast.next) {
      slow = slow.next
      fast = fast.next.next
   }
   return slow
}