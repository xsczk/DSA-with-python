"""Given a string expression of numbers and operators,
return all possible results from computing all the different possible ways
to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer
and the number of different results does not exceed 104.

Constraints:
- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
- The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

"""


class Solution:
    def diff_ways_to_compute(self, expression: str) -> list[int]:
        results = []
        # first base case: if the string is empty, return an empty list
        if len(expression) == 0: return results
        # second base case: if the expression is a single digit, return a list with that number
        if len(expression) == 1: return [int(expression)]
        # third base case: if the expression has two characters and the first is a digit
        # the second must also be a digit so we convert this expression to a number
        # and return it in a list
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]
        for i, char in enumerate(expression):
            # skip if the current character is a digit
            if char.isdigit(): continue
            # split the expression into left and right parts
            left_results = self.diff_ways_to_compute(expression=expression[:i])
            right_results = self.diff_ways_to_compute(expression=expression[i + 1:])
            for left in left_results:
                for right in right_results:
                    # perform the operation based on the current character (+, -, *)
                    if char == '*':
                        results.append(left * right)
                    elif char == '+':
                        results.append(left + right)
                    else:
                        results.append(left - right)
        return results

solution = Solution()
all_results = solution.diff_ways_to_compute("2*3-4*5")
print(all_results)