class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "Was it a car or a cat I saw?"
        l = 0
        r = len(s) - 1
        while l < r:
            valid_l, valid_r = s[l].isalnum(), s[r].isalnum()

            if not valid_l and not valid_r:
                l += 1
                r -= 1
            elif not valid_l:
                l += 1
            elif not valid_r:
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True