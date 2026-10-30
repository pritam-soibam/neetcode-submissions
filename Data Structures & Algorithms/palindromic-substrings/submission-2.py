class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_outwards(left, right, count=0):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        count = 0
        for i in range(len(s)):
            count += expand_outwards(left=i, right=i)  # handles odd palindromes
            count += expand_outwards(left=i, right=i + 1)  # handles even palindromes
        return count
