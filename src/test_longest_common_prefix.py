"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Reference: https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        match len(strs):
            case 0:
                return ""
            case 1:
                return strs[0]

        def _match_recursion(left: int, right: int) -> int:
            if left >= right:
                return left

            # Visit the left partition:
            middle: int = left + (right - left) // 2
            if left < middle:
                match_len: int = _match_recursion(left, middle)
                if match_len < middle:
                    return match_len
            
            # Test the current column:
            ref_ch: str = strs[0][middle]
            if any(
                ref_ch != strs[j][middle] 
                for j in range(1, len(strs))
            ):
                return middle
            
            # Visit the right partition:
            return _match_recursion(middle + 1, right)
                
        min_len: int = min(len(s) for s in strs)
        match_len: int = _match_recursion(0, min_len)
        return strs[0][:match_len]


def test_solution():
    solution = Solution()
    
    # Test case 1: Common prefix exists
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    
    # Test case 2: No common prefix
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    
    # Test case 3: Single string
    assert solution.longestCommonPrefix(["hello"]) == "hello"
    
    # Test case 4: Empty list
    assert solution.longestCommonPrefix([]) == ""
    
    # Test case 5: All strings identical
    assert solution.longestCommonPrefix(["test", "test", "test"]) == "test"
    
    # Test case 6: One character common prefix
    assert solution.longestCommonPrefix(["a", "a", "a"]) == "a"
    
    # Test case 7: Entire first string is prefix
    assert solution.longestCommonPrefix(["ab", "a"]) == "a"
    
    # Test case 8: Longer common prefix
    assert solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
