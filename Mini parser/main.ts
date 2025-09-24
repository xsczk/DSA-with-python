// @ts-ignore
/**
 * Given a string s represents the serialization of a nested list, implement a parser
 * to deserialize it and return the deserialized NestedInteger.
 *
 * Each element is either an integer or a list whose elements may also be integers or other lists.
 *
 * Example:
 * - Input: s = "[123,[456,[789]]]"
 * - Output: [123,[456,[789]]]
 * Explanation: Return a NestedInteger object containing a nested list with 2 elements:
 * 1. An integer containing value 123.
 * 2. A nested list containing two elements:
 *     i.  An integer containing value 456.
 *     ii. A nested list with one element:
 *          a. An integer containing value 789
 *
 * Constraints:
 * - 1 <= s.length <= 5 * 104
 * - s consists of digits, square brackets "[]", negative sign '-', and commas ','.
 * - s is the serialization of valid NestedInteger.
 * - All the values in the input are in the range [-10^6, 10^6].
 */

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
   // If value is provided, then it holds a single integer
   // Otherwise it holds an empty nested list
   constructor(value?: number) {

   };

   // Return true if this NestedInteger holds a single integer, rather than a nested list.
   // @ts-ignore
   isInteger(): boolean {

   };

   //  Return the single integer that this NestedInteger holds, if it holds a single integer
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

   //  Return the nested list that this NestedInteger holds,
   // or an empty list if this NestedInteger holds a single integer
   // @ts-ignore
   getList(): NestedInteger[] {

   };
}


function deserialize(s: string): NestedInteger {
   if (!s.startsWith('[')) {
      return new NestedInteger(Number(s))
   }
   let i = 0
   const stack: NestedInteger[] = [new NestedInteger()]
   while (i < s.length) {
      if (s[i] == ',') {
         i += 1
         continue
      }
      if (s[i] == '[') {
         const newList = new NestedInteger()
         stack.at(-1)?.add(newList)
         // the newList element becomes the current NestedInteger we are working on
         stack.push(newList)
      } else if (s[i] == ']') {
         stack.pop()
      } else {
         let j = i
         // we can guarantee s[j] is now only a digit or negative sign '-'
         while (j < s.length && (s[j] == '-' || !isNaN(Number(s[j])))) {
            j += 1
         }
         const integer = Number(s.slice(i, j))
         stack.at(-1)?.add(new NestedInteger(integer))
         // skip i and turn i to the character after the last digit inside the while loop
         i = j
         continue
      }
      i += 1
   }
   return stack[0].getList()[0]
};