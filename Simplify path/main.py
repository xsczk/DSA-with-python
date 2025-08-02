"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

- A single period '.' represents the current directory.
- A double period '..' represents the previous/parent directory.
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
- Any sequence of periods that does not match the rules above should be treated
as a valid directory or file name.
For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash '/'.
- Directories within the path must be separated by exactly one slash '/'.
- The path must not end with a slash '/', unless it is the root directory.
- The path must not have any single or double periods ('.' and '..') used to denote
current or parent directories.

Return the simplified canonical path.

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.
"""


class Solution:
    # stack, string
    # time complexity: O(n)
    # space complexity: O(n)
    def simplify_path(self, path: str) -> str:
        directories = path.split('/')
        stack = []
        for directory in directories:
            # if the directory is a valid file name, push it to stack
            if directory not in ("..", ".", ""):
                stack.append(directory)
            # need to go to the previous directory
            elif directory == '..' and stack:
                stack.pop()
        return "/" + "/".join(stack)


solution = Solution()
print(solution.simplify_path("/home/user/Documents/../Pictures"))
