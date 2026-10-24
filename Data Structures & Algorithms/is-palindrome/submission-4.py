class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "Was it a car or a cat I saw?"
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() is False and s[r].isalnum() is False:
                l += 1
                r -= 1
            elif s[l].isalnum() is False:
                l += 1
            elif s[r].isalnum() is False:
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True