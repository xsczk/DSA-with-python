/**
 * There are n persons on a social media website. You are given an integer array ages
 * where ages[i] is the age of the ith person.
 *
 * A Person x will not send a friend request to a person y (x != y)
 * if any of the following conditions is true:
 *
 * - age[y] <= 0.5 * age[x] + 7
 * - age[y] > age[x]
 * - age[y] > 100 && age[x] < 100 (This condition is redundant)
 * Otherwise, x will send a friend request to y.
 *
 * Note that if x sends a request to y, y will not necessarily send a request to x.
 * Also, a person will not send a friend request to themself.
 *
 * Return the total number of friend requests made.
 *
 * Constraints:
 * - n == ages.length
 * - 1 <= n <= 2 * 10^4
 * - 1 <= ages[i] <= 120
 */

// apply the same logic of binary search and two pointers from python approach
function numFriendRequests(ages: number[]): number {
   ages.sort((a, b) => a - b)
   const numRequestsFromAge = {}
   let ans = 0, n = ages.length
   ages.forEach((age, i) => {
      if (age < 15 || numRequestsFromAge[age]) {
         ans += numRequestsFromAge[age] ?? 0
         // since forEach will execute the callback for each element
         // we simply use return to skip and move to the next iteration
         return
      }
      let l = 0, r = n - 1
      let leftMostValidIndex = l
      while (l <= r) {
         const mid = Math.floor((l + r) / 2)
         // find the lower bound aka the first index that ages[y] > 0.5 * age + 7
         if (ages[mid] > 0.5 * age + 7) {
            leftMostValidIndex = mid
            r = mid - 1
         } else {
            l = mid + 1
         }
      }
      l = 0
      r = n - 1
      let rightMostValidIndex = r
      while (l <= r) {
         const mid = Math.floor((l + r) / 2)
         // find the upper bound aka the last index that ages[y] <= age
         if (ages[mid] <= age) {
            rightMostValidIndex = mid
            l = mid + 1
         } else {
            r = mid - 1
         }
      }
      const validRequests = Math.max(rightMostValidIndex - leftMostValidIndex, 0)
      ans += validRequests
      numRequestsFromAge[age] = validRequests
   })
   return ans
}

console.log(numFriendRequests([20, 30, 30, 100, 100, 110, 110, 110, 120]))