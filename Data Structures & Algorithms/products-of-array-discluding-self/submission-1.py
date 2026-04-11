import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], []
        i, j = 1, 1
        for num in nums:
            prefix.append(i)
            i *= num
        for num in reversed(nums):
            postfix.append(j)
            j *= num
        print(prefix)
        print(postfix)
        res = []
        for k in range(len(nums)):
            res.append(prefix[k] * postfix[len(nums) - k - 1])
        return res


        [1, 1, 2, 8, 48]
        [48, 24, 6, 1]

        [1, -1, 0, 0, 0, 0]
        [0, 6, 6, 3, 1]
        