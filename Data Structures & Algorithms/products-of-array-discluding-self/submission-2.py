import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix, postfix = 1, 1
        i, j = 1, 1
        for num in nums:
            res.append(i)
            i *= num
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        print(prefix)
        print(postfix)
        return res
        