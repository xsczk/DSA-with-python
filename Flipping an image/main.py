"""
Given an n x n binary matrix image, flip the image horizontally, then invert it,
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

Constraints:
n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
"""


class Solution:
    def flip_and_invert_image(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                # special case for row has odd elements
                if i == j:
                    row[i] = int(not row[i])
                    break
                # reverse and flip each row
                row[i], row[j] = int(not row[j]), int(not row[i])
                i += 1
                j -= 1
        return image

    # flipping an image using XOR operator
    def flip_and_invert_image_2(self, image: list[list[int]]) -> list[
        list[int]]:
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                # special case for row has odd elements
                if i == j:
                    row[i] = row[i] ^ 1
                    break
                # reverse and flip each row
                row[i], row[j] = row[j] ^ 1, row[i] ^ 1
                i += 1
                j -= 1
        return image

    # using for loop instead of while loop
    def flip_and_invert_image_3(self, image: list[list[int]]) -> list[
        list[int]]:
        for row in image:
            for i in range((len(row) + 1) // 2):
                # in python, ~i is equivalent to -i - 1 or len(row) - i - 1
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image


solution = Solution()
print(solution.flip_and_invert_image_3(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
