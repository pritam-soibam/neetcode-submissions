class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1 or s == s[::-1]:
            return s

        palindrome = ""

        def wrapAround(l, r, palindrome):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(palindrome) < r+1-l:
                    palindrome = s[l:r+1]
                l -=1 
                r +=1
            return palindrome

        for i in range(len(s)):
            palindrome = wrapAround(i, i, palindrome) # # odd palindrome: ibobi
            palindrome = wrapAround(i, i+1, palindrome) # even palindrome: iboobi
        
        return palindrome