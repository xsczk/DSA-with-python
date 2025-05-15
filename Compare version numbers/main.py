"""Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order.
If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0."""


class Solution:
    def compare_version(self, version1: str, version2: str) -> int:
        # create two list contains all revisions values
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        n1, n2 = len(ver1), len(ver2)
        max_len = max(n1, n2)

        for i in range(max_len):
            # compare each revision value, if one of the version has fewer revisions,
            # we fill it with 0 and compare it with other version's revision
            # until we reach the max length
            v1 = int(ver1[i]) if i < n1 else 0
            v2 = int(ver2[i]) if i < n2 else 0
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0

solution = Solution()
ans = solution.compare_version(version1='1.0.2', version2='1.1.01')
print(ans)