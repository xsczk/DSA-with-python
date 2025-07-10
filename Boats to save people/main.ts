/**
 * You are given an array people where people[i] is the weight of the ith person,
 * and an infinite number of boats where each boat can carry a maximum weight of limit.
 * Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
 *
 * Return the minimum number of boats to carry every given person.
 */

function num_rescue_boats(people: number[], limit: number): number {
   people.sort((a, b) => a - b)
   let l = 0, r = people.length - 1
   let boats = 0
   while (l <= r) {
      const weight = people[l] + people[r]
      if (weight <= limit) {
         l++
      }
      r--
      boats++
   }
   return boats
}