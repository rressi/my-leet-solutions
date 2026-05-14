"""
Given two integers dividend and divisor, divide two integers without using 
multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Return the quotient after dividing dividend by divisor.

Reerence: https://leetcode.com/problems/divide-two-integers/
"""


MAX_INT = 2**31 - 1
MIN_INT = -2**31

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor

        if dividend < divisor:
            return 0

        result: int = 1
        accumulator: int = divisor

        while (accumulator << 1) <= dividend:
            accumulator = (accumulator << 1)
            result = result << 1

        while accumulator + divisor <= dividend:
            accumulator += divisor
            result += 1

        if sign < 0:
            result = -result

        return min(max(result, MIN_INT), MAX_INT)


def test_solution():
    solution = Solution()
    assert solution.divide(10, 3) == 3
    assert solution.divide(7, -3) == -2
    assert solution.divide(0, 1) == 0
    assert solution.divide(1, 1) == 1
    assert solution.divide(-2147483648, -1) == MAX_INT
    assert solution.divide(-2147483648, 1) == MIN_INT

if __name__ == "__main__":
    test_solution()
