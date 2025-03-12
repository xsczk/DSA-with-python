"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store."""

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def max_area(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            current_area = h * w
            max_area = max(max_area, current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

solution = Solution()
result = solution.max_area(height = [2, 1, 8, 6, 4, 6, 5, 5])
print(result)