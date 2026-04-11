from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        return sorted(res, key=res.get, reverse=True)[:k]