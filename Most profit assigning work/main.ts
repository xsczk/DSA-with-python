/**
 * You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
 *
 * - difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
 * - worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job
 * with difficulty at most worker[j]).
 * Every worker can be assigned at most one job, but one job can be completed multiple times.
 *
 * - For example, if three workers attempt the same job that pays $1,
 * then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
 * Return the maximum profit we can achieve after assigning the workers to the jobs.
 *
 * Constraints:
 * - n == difficulty.length
 * - n == profit.length
 * - m == worker.length
 * - 1 <= n, m <= 10^4
 * - 1 <= difficulty[i], profit[i], worker[i] <= 10^5
 */

// approach 1: binary search, sort by difficulty
function maxProfitAssignment(difficulty: number[], profit: number[],
                             worker: number[]): number {
   const n = difficulty.length
   const jobProfile = [[0, 0]]
   for (const i in difficulty) {
      jobProfile.push([difficulty[i], profit[i]])
   }
   // sort jobProfile by difficulty
   jobProfile.sort((a, b) => {
      return a[0] - b[0]
   })
   const m = jobProfile.length - 1
   // update the current jobProfile profit value with the greater value
   // between it and its previous value
   for (let i = 0; i < m; i++) {
      jobProfile[i + 1] = [
         jobProfile[i + 1][0], Math.max(jobProfile[i + 1][1], jobProfile[i][1])
      ]
   }
   let netProfit = 0
   for (const ability of worker) {
      let l = 0, r = m, maxProfit = 0
      // find the most difficult job a worker can handle using binary search
      while (l <= r) {
         const mid = Math.floor((l + r) / 2)
         if (jobProfile[mid][0] <= ability) {
            maxProfit = jobProfile[mid][1]
            l = mid + 1
         } else {
            r = mid - 1
         }
      }
      netProfit += maxProfit
   }
   return netProfit
}

// two pointers, greedy
function maxProfitAssignment3(...params: Parameters<typeof maxProfitAssignment>): number {
   const [difficulty, profit, worker] = params
   const jobProfile = difficulty.map((v, i) => {
      return [v, profit[i]]
   })
   jobProfile.sort((a, b) => a[0] - b[0])
   worker.sort((a, b) => a - b)
   let maxProfit = 0, netProfit = 0, j = 0
   for (const ability of worker) {
      while (j < difficulty.length && ability >= jobProfile[j][0]) {
         maxProfit = Math.max(maxProfit, jobProfile[j][1])
         j += 1
      }
      netProfit += maxProfit
   }
   return netProfit
}

console.log(maxProfitAssignment3([68, 35, 52, 47, 86], [67, 17, 1, 81, 3], [
   92, 10, 85, 84, 82
]))