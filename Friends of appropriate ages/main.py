"""
There are n persons on a social media website. You are given an integer array ages
where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y)
if any of the following conditions is true:

- age[y] <= 0.5 * age[x] + 7
- age[y] > age[x]
- age[y] > 100 && age[x] < 100 (This condition is redundant)
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x.
Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

Constraints:
- n == ages.length
- 1 <= n <= 2 * 10^4
- 1 <= ages[i] <= 120
"""
from collections import defaultdict


class Solution:
    # two pointers, binary search, sorting
    # time complexity: O(n * log n) for sorting and binary searching
    # space complexity: O(1) since requests_age will have max 120 keys from 1 to 120
    def numFriendRequests(self, ages: list[int]) -> int:
        # sort for binary searching
        ages.sort()
        ans, n = 0, len(ages)
        requests_age = defaultdict(int)
        for i, age in enumerate(ages):
            # skip if age < 15 because it is not able to find the lower bound
            if age < 15:
                continue
            # skip duplicate loop
            if age in requests_age:
                ans += requests_age[age]
                continue
            l, r = 0, n - 1
            left_most_valid_index = l
            while l <= r:
                mid = (l + r) // 2
                # find the lower bound: the first index where ages[y] > 0.5 * age + 7
                if ages[mid] > 0.5 * age + 7:
                    left_most_valid_index = mid
                    r = mid - 1
                else:
                    l = mid + 1
            l, r = 0, n - 1
            right_most_valid_index = r
            while l <= r:
                mid = (l + r) // 2
                # find the upper bound: the last index where ages[y] <= age
                if ages[mid] <= age:
                    right_most_valid_index = mid
                    l = mid + 1
                else:
                    r = mid - 1
            valid_requests = max(right_most_valid_index - left_most_valid_index,
                                 0)
            ans += valid_requests
            requests_age[age] = valid_requests
        return ans
