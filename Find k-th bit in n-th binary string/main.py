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
