"""
Given two integers dividend and divisor, divide two integers without using 
multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Return the quotient after dividing dividend by divisor.

Reerence: https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative: bool = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp_divisor = divisor
            num_divisors = 1
            
            # Trova il raddoppio più grande possibile per il resto attuale
            while (temp_divisor << 1) <= dividend:
                temp_divisor <<= 1
                num_divisors <<= 1
            
            # Sottrai il "blocco" più grande trovato
            dividend -= temp_divisor
            result += num_divisors
            
        if negative:
            return max(-result, -(1<<31))
        return min(result, (1<<31)-1)


def test_solution():
    solution = Solution()
    assert solution.divide(10, 3) == 3
    assert solution.divide(7, -3) == -2
    assert solution.divide(0, 1) == 0
    assert solution.divide(1, 1) == 1
    assert solution.divide(-2147483648, -1) == 2147483647
    assert solution.divide(-2147483648, 1) == -2147483648

if __name__ == "__main__":
    test_solution()
