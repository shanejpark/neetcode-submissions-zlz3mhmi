from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        return heapq.nlargest(k, res.keys(), key=res.get)