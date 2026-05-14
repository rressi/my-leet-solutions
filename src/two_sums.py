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
