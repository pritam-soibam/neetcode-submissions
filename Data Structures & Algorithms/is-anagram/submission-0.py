class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def mapAlphabets(word):
            alphabets = [0] * 26
            for alphabet in word:
                alphabets[ord(alphabet) - 97] += 1
            return alphabets
        return mapAlphabets(s) == mapAlphabets(t)