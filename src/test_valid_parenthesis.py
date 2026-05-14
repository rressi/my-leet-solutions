"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Reference: https://leetcode.com/problems/valid-parentheses/
"""
class OpenPar:
    pass

class Solution:

    def __init__(self):
        self.pairs = {
            '(': OpenPar(),
            '[': OpenPar(),
            '{': OpenPar(),
            ')': '(',
            ']': '[',
            '}': '{'
        }

    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for ch in s:
            match self.pairs.get(ch):
                case OpenPar():
                     # Open parenthesis
                    stack.append(ch)
                case str(expected_peer):
                    # Close parenthesis
                    actual_peer: str = stack.pop() if stack else None
                    if expected_peer != actual_peer:
                        return False  # Mismatched closing parenthesis
                case _:
                    return False  # Invalid character
            
        if stack:
            return False  # Unmatched opening brackets remain

        return True


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
