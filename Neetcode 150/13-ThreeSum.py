class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        op = []
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and n == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            print(l,r)
            while l < r:
                threeSum = nums[l] + nums[r] + n
                if threeSum == 0:
                    op.append([n, nums[l] ,nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return op
