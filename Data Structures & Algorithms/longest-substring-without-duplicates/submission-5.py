class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        i_map = {}
        res = 0

        for r in range(len(s)):
            if s[r] in i_map:
                l = max(l, i_map[s[r]] + 1)
            i_map[s[r]] = r
            res = max(res, r - l + 1)
        
        return res