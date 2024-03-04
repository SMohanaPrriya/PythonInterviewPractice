"""
Leet code : 70 Climbing stairs
You are climbing a staircase. It takes n steps to reach the top

Each time you can climb 1 or 2 steps. In how many distinct ways
can one climb to the top?

"""


class Solution:
    def getNumberOfWaysToClimb(self, n:int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = one
        return one


s = Solution()
print(s.getNumberOfWaysToClimb(3))