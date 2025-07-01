"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

- difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
- worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job
with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

- For example, if three workers attempt the same job that pays $1,
then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

Constraints:
- n == difficulty.length
- n == profit.length
- m == worker.length
- 1 <= n, m <= 10^4
- 1 <= difficulty[i], profit[i], worker[i] <= 10^5
"""


class Solution:
    # binary search, sort by difficulty
    # time complexity: O(n.logn + m.logn) where n.logn is complexity for sorting job_profile;
    # m.logn for binary search inside worker list loop
    def max_profit_assignment(self, difficulty: list[int], profit: list[int],
                              worker: list[int]) -> int:
        n = len(difficulty)
        job_profile = [(0, 0)]
        for i in range(n):
            job_profile.append((difficulty[i], profit[i]))
        # sort the job_profile based on job difficulty
        job_profile.sort(key=lambda x: x[0])
        m = len(job_profile) - 1
        # update the profit to keep the maximum profit a worker can get on their ability
        for i in range(m):
            job_profile[i + 1] = (job_profile[i + 1][0],
                                  max(job_profile[i + 1][1], job_profile[i][1]))
        net_profit = 0
        for ability in worker:
            l, r, max_profit = 0, m, 0
            # find the job with just smaller or equal difficulty than ability.
            while l <= r:
                mid = (l + r) // 2
                if job_profile[mid][0] <= ability:
                    max_profit = job_profile[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            net_profit += max_profit
        return net_profit


solution = Solution()
print(
    solution.max_profit_assignment(difficulty=[68, 35, 52, 47, 86],
                                   profit=[67, 17, 1, 81, 3],
                                   worker=[92, 10, 85, 84, 82]))
