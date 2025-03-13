"""You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person."""

# Time complexity: O(nlogn) -> due to sorting
# Space complexity: O(n) -> due to sorting
class Solution:
    def min_num_boats(self, people: list[int], limit: int) -> int:
        people.sort()
        heavy_p = len(people) - 1
        light_p = 0
        boats = 0
        while light_p <= heavy_p:
            if people[heavy_p] + people[light_p] <= limit:
                heavy_p -= 1
                light_p += 1
            else:
                heavy_p -= 1
            boats += 1
        return boats

solution = Solution()
result = solution.min_num_boats(people=[3,2,1,1], limit=4)
print(result)