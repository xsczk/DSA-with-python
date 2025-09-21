/**
 * You are given a nested list of integers nestedList. Each element is either an integer
 * or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
 *
 * Implement the NestedIterator class:
 *
 * - NestedIterator(List<NestedInteger> nestedList) Initializes the iterator
 * with the nested list nestedList.
 * - int next() Returns the next integer in the nested list.
 * - boolean hasNext() Returns true if there are still some integers in the nested list
 * and false otherwise.
 *
 * Your code will be tested with the following pseudocode:
 *
 * initialize iterator with nestedList
 * res = []
 * while iterator.hasNext()
 *     append iterator.next() to the end of res
 * return res
 *
 * - If res matches the expected flattened list, then your code will be judged as correct.
 *
 * Input: nestedList = [1,[4,[6]]]
 * Output: [1,4,6]
 * Explanation: By calling next repeatedly until hasNext returns false, the order of elements
 * returned by next should be: [1,4,6].
 *
 * Constraints:
 * - 1 <= nestedList.length <= 500
 * - The values of the integers in the nested list is in the range [-106, 106].
 */

class NestedInteger {
   // If value is provided, then it holds a single integer
   // Otherwise it holds an empty nested list
   constructor(value?: number) {

   };

   // Return true if this NestedInteger holds a single integer, rather than a nested list.
   // @ts-ignore
   isInteger(): boolean {

   };

   // Return the single integer that this NestedInteger holds, if it holds a single integer
   // Return null if this NestedInteger holds a nested list
   // @ts-ignore
   getInteger(): number | null {

   };

   // Set this NestedInteger to hold a single integer equal to value.
   setInteger(value: number) {

   };

   // Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
   add(elem: NestedInteger) {

   };

   // Return the nested list that this NestedInteger holds,
   // or an empty list if this NestedInteger holds a single integer
   // @ts-ignore
   getList(): NestedInteger[] {

   };
}

class NestedIterator {
   stack: NestedInteger[]

   constructor(nestedList: NestedInteger[]) {
      this.stack = []
      for (let i = nestedList.length - 1; i >= 0; i--) {
         this.stack.push(nestedList[i])
      }
   }

   hasNext(): boolean {
      while (this.stack.length) {
         const top = this.stack.at(-1)
         if (top?.isInteger()) {
            return true
         } else {
            const nestedList = this.stack.pop()?.getList() as NestedInteger[]
            for (let i = nestedList.length - 1; i >= 0; i--) {
               this.stack.push(nestedList[i])
            }
         }
      }
      return false
   }

   next(): number {
      return this.stack.pop()?.getInteger() as number
   }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new NestedIterator(nestedList)
 * var a: number[] = []
 * while (obj.hasNext()) a.push(obj.next());
 */