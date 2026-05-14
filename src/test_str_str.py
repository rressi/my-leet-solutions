"""
Given two strings needle and haystack, return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.

Reference: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        for i in range(len(haystack) - (len(needle) - 1)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


def test_solution():
    solution = Solution()
    assert solution.strStr("hello", "ll") == 2
    assert solution.strStr("aaaaa", "bba") == -1
    assert solution.strStr("", "") == -1
    assert solution.strStr("a", "") == -1
    assert solution.strStr("", "a") == -1
    assert solution.strStr("mississippi", "issip") == 4
    assert solution.strStr("mississippi", "issi") == 1
    assert solution.strStr("mississippi", "mississippi") == 0
    assert solution.strStr("mississippi", "mississippia") == -1


if __name__ == "__main__":
    test_solution()
