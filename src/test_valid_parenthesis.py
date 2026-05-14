"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Reference: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            match ch:
                case '(' | '[' | '{':
                    stack.append(ch)
                    continue
            try:
                match stack.pop() + ch:
                    case '()' | '[]' | '{}':
                        continue
                    case _:
                        return False
            except IndexError:
                return False

        return len(stack) == 0


def test_solution():
    solution = Solution()
    
    # Test case 1: Valid parentheses
    assert solution.isValid("()") is True
    
    # Test case 2: Valid nested parentheses
    assert solution.isValid("()[]{}") is True
    
    # Test case 3: Invalid parentheses
    assert solution.isValid("(]") is False
    
    # Test case 4: Invalid nested parentheses
    assert solution.isValid("([)]") is False
    
    # Test case 5: Single type of parentheses
    assert solution.isValid("{[]}") is True
    
    # Test case 6: Empty string
    assert solution.isValid("") is True

if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
