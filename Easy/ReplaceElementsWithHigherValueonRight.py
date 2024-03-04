#Leet code : 1299 Replace elements with greatest element on the right side

class Solution:
    def replaceWithGreatestElements(self, arr: list[int]) -> list[int]:
        maxValue = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(maxValue, arr[i])
            arr[i] = maxValue
            maxValue = newMax
        return arr


s = Solution()
print(s.replaceWithGreatestElements([17, 18, 5, 4, 6, 1]))