"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

"""

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    # Recursive approach
    def reverse_string(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return
        left, right = [0, len(s) - 1]

        def reverse(l: int, r: int):
            """Recursive until left indices is greater than right indices"""
            if l >= r:
                return
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            reverse(l + 1, r - 1)

        reverse(left, right)
