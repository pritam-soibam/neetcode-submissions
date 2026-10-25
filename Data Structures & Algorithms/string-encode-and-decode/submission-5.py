class Solution:
    
    def encode(self, strs: list[str]) -> str:
        s = ""
        for word in strs:
            s += f"{len(word)}${word}"
        return s

    def decode(self, s: str) -> list[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return strs
