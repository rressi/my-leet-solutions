"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, 
return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.

Reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n == 0:
            return 0

        last_i: int = 1
        last: int = nums[0]
        for i in range(1, len(nums)):
            cur: int = nums[i]
            if cur > last:
                nums[last_i] = cur
                last, last_i = cur, last_i + 1

        return last_i


def test_solution():
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [1, 1, 2]
    assert solution.removeDuplicates(nums1) == 2
    assert nums1[:2] == [1, 2]
    
    # Test case 2: All duplicates
    nums2 = [0, 0, 0, 0]
    assert solution.removeDuplicates(nums2) == 1
    assert nums2[:1] == [0]
    
    # Test case 3: No duplicates
    nums3 = [1, 2, 3, 4]
    assert solution.removeDuplicates(nums3) == 4
    assert nums3[:4] == [1, 2, 3, 4]
    
    # Test case 4: Empty array
    nums4 = []
    assert solution.removeDuplicates(nums4) == 0
    
    # Test case 5: Mixed duplicates
    nums5 = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums5) == 5
    assert nums5[:5] == [0,1,2,3,4]


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
