/**
 * Given an integer array arr, and an integer target,
 * return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
 *
 * As the answer can be very large, return it modulo 10^9 + 7.
 *
 * Constraints:
 * - 3 <= arr.length <= 3000
 * - 0 <= arr[i] <= 100
 * - 0 <= target <= 300
 */

function threeSumMulti(arr: number[], target: number): number {
   const MOD = 10 ** 9 + 7
   arr.sort((a, b) => a - b)
   // create an object of frequency counter
   const cnt = arr.reduce((res, num) => {
      res[num] = (res[num] ?? 0) + 1
      return res
   }, {})
   let ans = 0
   const n = arr.length
   for (let i = 0; i < n - 2; i++) {
      if (i && arr[i] == arr[i - 1]) continue
      const remain = target - arr[i]
      if (arr[i] > remain) break
      let j = i + 1, k = n - 1
      // binary search
      while (j < k) {
         const x = arr[i], y = arr[j], z = arr[k]
         if (y + z < remain) {
            j += cnt[y] - +(x == y)
         } else if (y + z > remain) {
            k -= cnt[z]
         } else {
            if (x != y && x != z && y != z) {
               ans += cnt[x] * cnt[y] * cnt[z]
            } else if (x == y && y != z) {
               ans += cnt[x] * (cnt[x] - 1) / 2 * cnt[z]
            } else if (x != y && y == z) {
               ans += cnt[x] * cnt[y] * (cnt[y] - 1) / 2
            } else {
               ans += cnt[x] * (cnt[x] - 1) * (cnt[x] - 2) / 6
            }
            j += cnt[y] - +(x == y)
            k -= cnt[z]
         }
      }
   }
   return ans % MOD
}

console.log(threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))