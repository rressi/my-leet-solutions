"""
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Reference: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = dict() # Hash map, O(1) insertion + search
        for j, y in enumerate(nums):
            match visited.get(target - y):
                case None:
                    visited[y] = j
                case int(i):
                    return [i, j]
        return None


def test_solution():
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: Different target
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3: Negative numbers
    assert solution.twoSum([-1, -2, -3, 5, 10], 7) == [2, 4]
    
    # Test case 4: Large numbers
    assert solution.twoSum([1000000, 2000000, 3000000], 4000000) == [0, 2]


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
