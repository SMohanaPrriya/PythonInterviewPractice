"""
Leet code: 53 Maximum sub array
Given integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum

nums - can contain negative numbers.
similar to sliding window concept.
"""


class Solution:
    def getMaximumSubarray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum


s = Solution()
print(s.getMaximumSubarray([1, 2, 3, 4, -11]))
print(s.getMaximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, -4]))
