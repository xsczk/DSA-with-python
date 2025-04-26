"""Given two positive integers n and k, the binary string Sn is formed as follows:

- S1 = "0"
- Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x,
and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n."""


class Solution:
    # iterative brute force
    # Time complexity: O(2^n) since we create a string with 2^n - 1 length in each interation (worst case)
    # Space complexity: O(2^n)
    def find_kth_bit(self, n: int, k: int) -> str:
        sequence = "0"
        for i in range(n):
            if k <= len(sequence):
                break
            sequence += "1"
            cur = ["1" if bit == "0" else "0" for bit in sequence[:-1]]
            sequence += ''.join(cur[::-1])
        return sequence[k - 1]

    # recursion
    # Time complexity: O(n) - we decrease n by 1 in each call until we reach the base case where n is 1
    # Space complexity: O(n) - due to recursion stack
    def find_kth_bit_2(self, n: int, k: int) -> str:
        # base case: for S1
        if n == 1: return '0'
        total = 2 ** n - 1
        # base case: if k is in exactly middle position
        if k == (total // 2) + 1:
            return '1'
        elif k <= (total // 2):
            # recursively call with left half binary string
            return self.find_kth_bit_2(n - 1, k)
        # recursively call with right half binary string
        # k = total - k + 1 means we find the bit at the position of the same left half binary string in inverted form
        inverted = self.find_kth_bit_2(n - 1, total - k + 1)
        return '1' if inverted == '0' else '0'

    # iterative divide and conquer based on the recursion version
    # Time complexity: O(n)
    # Space complexity: O(1) since we do not need recursion
    """
        011100110110001      invert = False
                  I
        0111001              invert = True
            I
        011                  invert = False
          I
        0                    invert = True
        I
    """
    def find_kth_bit_3(self, n: int, k: int) -> str:
        invert = False
        total = 2 ** n - 1
        while k > 1:
            # if k is in the middle, return based on invert variable
            if k == total // 2 + 1:
                return '1' if not invert else '0'
            # if k is in the second half, invert and mirror
            elif k > total // 2:
                k = total - k + 1   # mirror position
                invert = not invert # flip
            # reduce length for next iteration
            total //= 2
        # for the first position, return based on invert variable
        return '1' if invert else '0'

