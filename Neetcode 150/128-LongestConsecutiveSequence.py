class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique = set(nums)
        maxCount = 0
        for n in nums:
            if n-1 not in unique:
                count = 1
                while n + count in unique:
                    count += 1
                maxCount = max(count, maxCount)
        return maxCount