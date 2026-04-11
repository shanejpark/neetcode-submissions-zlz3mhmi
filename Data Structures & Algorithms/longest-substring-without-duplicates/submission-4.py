class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        while l <= len(s):
            if len(s[l:r+1]) == len(set(s[l:r+1])) and r != len(s):
                res = max(len(s[l:r+1]), res)
                r += 1
            else:
                l += 1
        return res