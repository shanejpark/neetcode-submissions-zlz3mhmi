from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        resl, resr = -1, -1
        l = 0
        havemap, needmap = Counter(), Counter(t)
        have, need = 0, len(needmap)
        for r in range(len(s)):
            if s[r] in needmap:
                havemap[s[r]] += 1
                if havemap[s[r]] == needmap[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1 < resr - resl + 1 or resl == resr == -1):
                    resl, resr = l, r
                if s[l] in needmap:
                    if havemap[s[l]] == needmap[s[l]]:
                        have -= 1
                    havemap[s[l]] -= 1
                l += 1

        return s[resl:resr+1]
            
