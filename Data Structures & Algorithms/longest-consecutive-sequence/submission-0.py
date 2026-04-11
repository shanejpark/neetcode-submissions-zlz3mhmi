class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0
        for num in numset:
            if num - 1 not in numset:
                current = num
                length = 1
                while current + 1 in numset:
                    current += 1
                    length += 1
                max_length = max(max_length, length)
        return max_length
