class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_list = [0] * 26
        for i in range(len(s)):
            char_list[ord(s[i]) - ord('a')] += 1
            char_list[ord(t[i]) - ord('a')] -= 1
        for i in range(len(char_list)):
            if char_list[i] != 0:
                return False
        return True
        