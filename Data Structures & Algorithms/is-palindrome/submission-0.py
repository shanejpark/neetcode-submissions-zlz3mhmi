class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [c for c in s if c.isalnum()]
        i, j = 0, len(filtered_chars) - 1
        while i < (len(filtered_chars) - 1)/2:

            if filtered_chars[i].casefold() != filtered_chars[j].casefold():
                print(filtered_chars[i] + filtered_chars[j])
                return False
            i += 1
            j -= 1
        return True
