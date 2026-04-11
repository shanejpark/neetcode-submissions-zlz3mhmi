from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freqs1 = Counter(s1)
        freqs2 = Counter(s2[0:len(s1)])
        for l in range(len(s2) - len(s1)):
            if freqs1 == freqs2:
                return True
            freqs2[s2[l]] -= 1
            freqs2[s2[l + len(s1)]] += 1
        return freqs1 == freqs2
            
            

            

        