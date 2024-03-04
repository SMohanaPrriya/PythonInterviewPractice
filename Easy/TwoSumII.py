"""
Leet code: 167 Two SUM - II - Input array is sorted

assume - each input exactly has one solution
"""

class Solution:
    def getTwoSumWithInputSorted(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums)-1
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum == target:
                return [left+1, right+1]
            elif currSum > target:
                right -= 1
            else:
                left += 1


s = Solution()
print(s.getTwoSumWithInputSorted([1, 3, 4, 5, 7, 10, 11], 9))