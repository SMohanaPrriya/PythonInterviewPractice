#Leet code : 7 - ReverseInteger ufor the 32-bit integer
import math
class Solution:
    def reverseInteger(self, n: int) -> int:
        MIN = -2147483648 # -2^31
        MAX = 2147483647  #  2^31-1
        res = 0
        while n:
            digit = int(math.fmod(n, 10))
            n = int(n/10)

            if(res > MAX//10 or
                    (res == MAX//10 and digit >= MAX % 10)):
                return 0

            if(res < MIN//10 or
                    (res == MIN//10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return res


s = Solution()
print(s.reverseInteger(123))
print(s.reverseInteger(123123123))