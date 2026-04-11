class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        this_dict = {}
        for i, num in enumerate(nums):
            if num in this_dict:
                return [this_dict[num], i]
            this_dict[target - num] = i 


        