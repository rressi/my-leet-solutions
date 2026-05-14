"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Reference: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:

    def __init__(self):
        self.values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        result = 0
        max_value = 0
        for digit in reversed(s):
            try:
                value = self.values[digit]
            except KeyError as ex:
                raise ValueError(
                    f"Unexpected roman digit: {digit}"
                ) from ex
            if max_value > value:
                result -= value
            else:
                result += value
                max_value = value
        return result


def test_roman_to_int():
    solution = Solution()

    # Basic symbols
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58

    # Subtractive notation
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("MCMXCIV") == 1994

    # Larger value with mixed notation
    assert solution.romanToInt("MMXXVI") == 2026

    # Edge behavior for empty string in current implementation
    assert solution.romanToInt("") == 0

    # Invalid characters should raise ValueError
    try:
        solution.romanToInt("A")
        assert False, "Expected ValueError for invalid Roman numeral"
    except ValueError:
        pass


if __name__ == "__main__":
    test_roman_to_int()
    print("All tests passed!")

