class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = dict()
        for i,n in enumerate(nums):
            num = target - n
            if num in diff:
                return [diff[num], i]
            diff[n]=i
