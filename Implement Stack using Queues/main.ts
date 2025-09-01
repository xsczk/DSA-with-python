/**
 * Implement a last-in-first-out (LIFO) stack using only two queues.
 * The implemented stack should support all the functions of a normal stack
 * (push, top, pop, and empty).
 *
 * Implement the MyStack class:
 * - void push(int x) Pushes element x to the top of the stack.
 * - int pop() Removes the element on the top of the stack and returns it.
 * - int top() Returns the element on the top of the stack.
 * - boolean empty() Returns true if the stack is empty, false otherwise.
 *
 * Notes:
 * - You must use only standard operations of a queue, which means that only push to back,
 * peek/pop from front, size and is empty operations are valid.
 * - Depending on your language, the queue may not be supported natively.
 * You may simulate a queue using a list or deque (double-ended queue) as long as
 * you use only a queue's standard operations.
 *
 * Constraints:
 * - 1 <= x <= 9
 * - At most 100 calls will be made to push, pop, top, and empty.
 * - All the calls to pop and top are valid.
 */

class MyStack {
   q: number[]

   constructor() {
      this.q = []
   }

   push(x: number): void {
      this.q.push(x)
      /** [1, 2, 3] => [3, 1, 2] */
      for (let i = 0; i < this.q.length - 1; i++) {
         /** using shift to simulate peek method */
         this.q.push(this.q.shift() as number)
      }
   }

   pop(): number {
      /** all the calls to pop and top are valid */
      return this.q.shift() as number
   }

   top(): number {
      return this.q[0]
   }

   empty(): boolean {
      return this.q.length === 0
   }
}