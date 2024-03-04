"""
Leet code : 198 house robber
robber cannot rob adjacent houses, such that max that he can steal
"""

class Solution:
    def getMaxMoneyForHouseRobber(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


s = Solution()
print(s.getMaxMoneyForHouseRobber([1, 2, 3, 1]))
