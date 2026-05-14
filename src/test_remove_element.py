"""
Given an integer array nums and an integer val, remove all occurrences of val in 
nums in-place. The order of the elements may be changed. Then return the number of 
elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get 
accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements 
  which are not equal to val. The remaining elements of nums are not important as 
  well as the size of nums.
- Return k.

Reference: https://leetcode.com/problems/remove-element/description/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Best runtime: N
        # Best memory complexity: 1
        i: int = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


def test_solution():
    solution = Solution()
    assert solution.removeElement([3, 2, 2, 3], 3) == 2
    assert solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert solution.removeElement([0, 1, 2, 3, 4], 5) == 5
    assert solution.removeElement([0, 1, 2, 3, 4], 0) == 4
    assert solution.removeElement([0, 1, 2, 3, 4], 4) == 4
    assert solution.removeElement([0, 0, 0, 0, 0], 0) == 0


if __name__ == "__main__":
    test_solution()
