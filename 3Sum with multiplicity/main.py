"""
Given an integer array arr, and an integer target,
return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 3 <= arr.length <= 3000
- 0 <= arr[i] <= 100
- 0 <= target <= 300
"""
from collections import Counter


class Solution:
    # two pointers, hash table, mathematics
    # time complexity: O(n^2)
    # space complexity: O(n) due to cnt object
    def three_sum_multi(self, arr: list[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        res, n = 0, len(arr)
        cnt = Counter(arr)
        for i in range(n - 2):
            # skip duplicates:
            if i and arr[i] == arr[i - 1]:
                continue
            remain = target - arr[i]
            # break from the loop since the arr is sorted
            if arr[i] > remain:
                break
            j, k = i + 1, n - 1
            # binary search
            while j < k:
                x, y, z = arr[i], arr[j], arr[k]
                if y + z < remain:
                    # need to minus 1 if we are at the element which is the same value with the previous
                    # ex: 1, 1, 1, 2
                    #        j          count[1] = 3
                    #          ->  j
                    j += cnt[y] - (x == y)
                elif y + z > remain:
                    k -= cnt[z]
                else:
                    # use combinatorics
                    if x != y != z:
                        res += cnt[x] * cnt[y] * cnt[z]
                    elif x == y != z:
                        res += cnt[x] * (cnt[x] - 1) // 2 * cnt[z]
                    elif x != y == z:
                        res += cnt[x] * cnt[y] * (cnt[y] - 1) // 2
                    else:  # x == y == z
                        res += cnt[x] * (cnt[x] - 1) * (cnt[x] - 2) // 6
                    j += cnt[y] - (x == y)
                    k -= cnt[z]
        return res % MOD
