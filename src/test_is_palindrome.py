class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits: str = str(x)
        half_size: int = len(digits) // 2
        for i, (a, b) in enumerate(zip(
            iter(digits),
            reversed(digits)
        )):
            if i >= half_size:
                return True
            if a != b:
                return False


def test_solution():
    solution = Solution()
    
    # Test case 1: Palindrome with even length
    assert solution.isPalindrome(121) is True
    
    # Test case 2: Non-palindrome
    assert solution.isPalindrome(123) is False
    
    # Test case 3: Single digit (always palindrome)
    assert solution.isPalindrome(7) is True
    
    # Test case 4: Large palindrome
    assert solution.isPalindrome(1001) is True
    
    # Test case 5: Number ending in 0 (not palindrome)
    assert solution.isPalindrome(10) is False
    
    # Test case 6: Negative number (not palindrome)
    assert solution.isPalindrome(-121) is False
    
    # Test case 7: Zero
    assert solution.isPalindrome(0) is True


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
