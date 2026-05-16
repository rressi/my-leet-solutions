"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
import re

CHAR_0: int = ord('0')
DECIMAL_MATCHER = re.compile(r"^\s*([+-]?)0*(\d{1,11})")

class Solution:
    def myAtoi(self, s: str) -> int:
        if match := DECIMAL_MATCHER.match(s):
            sign, digits = match.groups()
            result: int = 0
            for ch in digits:
                result = result * 10 + ord(ch) - CHAR_0
            return (
                max(-2147483648, -result) if sign == '-'
                else min(2147483647, result)
            )
        else:
            return 0

def test_solution():
    sol = Solution()
    # Basic cases
    assert sol.myAtoi("42") == 42
    assert sol.myAtoi("   -42") == -42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("-91283472332") == -2147483648
    assert sol.myAtoi("91283472332") == 2147483647
    assert sol.myAtoi("+00000123") == 123
    assert sol.myAtoi("  +0 123") == 0
    assert sol.myAtoi("") == 0
    assert sol.myAtoi("+") == 0
    assert sol.myAtoi("-") == 0
    assert sol.myAtoi("  0000000000012345678") == 12345678

    # Edge cases: smallest possible number with 11 and 10 decimal digits
    assert sol.myAtoi("-10000000000") == -2147483648  # 11 digits, should clamp to INT_MIN
    assert sol.myAtoi("-1000000000") == -1000000000   # 10 digits, should parse as is

    # Edge cases: largest possible number with 11 and 10 decimal digits
    assert sol.myAtoi("10000000000") == 2147483647    # 11 digits, should clamp to INT_MAX
    assert sol.myAtoi("1000000000") == 1000000000     # 10 digits, should parse as is

if __name__ == "__main__":
    test_solution()
