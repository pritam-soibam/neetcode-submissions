class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        seen = {}
        left = 0
        for right in range(len(s)):
            substring = s[right]
            if substring in seen:
                left = max(seen[substring] + 1, left)
            length = max(length, right - left + 1)
            seen[substring] = right
        
        return length