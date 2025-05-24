"""Winter is coming! During the contest, your first job is to design a standard heater
with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of houses and heaters on a horizontal line,
return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

Constraints:
- 1 <= houses.length, heaters.length <= 3 * 10^4
- 1 <= houses[i], heaters[i] <= 10^9
"""


class Solution:
    # sorting, binary search
    # Time complexity: O(n*log h) where n is the len of houses,
    # h is the len of heaters for binary search
    def find_radius(self, houses: list[int], heaters: list[int]) -> int:
        # sort the heaters for using binary search
        heaters.sort()
        radius = 0
        for house in houses:
            l, r = 0, len(heaters) - 1
            # find the minimum distance from each house to the closest heater
            while l < r:
                mid = (l + r) // 2
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid
            distance = abs(heaters[l] - house)
            # handle special case
            if l > 0:
                distance = min(distance, abs(heaters[l - 1] - house))
            # get max radius to could over all houses
            radius = max(radius, distance)
        return radius

    # sorting, two pointers
    # Time complexity: O(n log n + h log h) - n is the len of houses, h is the len of heaters
    # Space complexity: O(1)
    def find_radius_2(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        houses.sort()
        radius = 0
        i = 0
        # For each house, find the closest heater (using a pointer i that only moves forward)
        # and update the maximum required radius.
        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            # get the max of current radius heaters and current max radius value
            radius = max(radius, abs(heaters[i] - house))
        return radius
