"""Given an array of integers, return indices of two numbers
such that they add up to the target. IT has only one solution

Input: List and integer
Output: List containing two indexes
"""


class Solution:
    def gettwosum(self, nums: list[int], target: int) -> list[int]:
        value_index = {} # value: index
        for index, num in enumerate(nums):
            diff = target - num
            #check if the difference(another number in the list) is already seen.
            if diff in value_index:
                return [value_index[diff], index]
            value_index[num] = index
        return []


s = Solution()
print(s.gettwosum([1, 2, 3, 4], 6))
print(s.gettwosum([2, 7, 11, 15], 26))
print(s.gettwosum([1, 7, 11, 15], 12))
