/**
 * Given an n x n binary matrix image, flip the image horizontally, then invert it,
 * and return the resulting image.
 *
 * To flip an image horizontally means that each row of the image is reversed.
 *
 * For example, flipping [1,1,0] horizontally results in [0,1,1].
 * To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
 *
 * For example, inverting [0,1,1] results in [1,0,0].
 *
 * Constraints:
 * n == image.length
 * n == image[i].length
 * 1 <= n <= 20
 * images[i][j] is either 0 or 1.
 */

function flipAndInvertImage(image: number[][]): number[][] {
   for (const row of image) {
      for (let i = 0; i < Math.floor((row.length + 1) / 2); i++) {
         const swapIndex = row.length - i - 1
         const temp = row[i] ^ 1
         row[i] = row[swapIndex] ^ 1
         row[swapIndex] = temp
      }
   }
   return image
}

console.log(flipAndInvertImage([
   [1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]
]))