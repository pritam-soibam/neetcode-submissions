class Solution:

    def attempt1(self, s: str):
        letters = []
        known = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for ch in s.lower():
            if ch not in known:
                continue
            letters.append(ch)

        mid = len(letters) // 2
        if len(letters) % 2 == 0:
            l, r = mid - 1, mid
        else:
            l = r = mid

        print("starting from:", l, r)
        while l >= 0 and r < len(letters):
            if letters[l] == letters[r]:
                l -= 1
                r += 1
            else:
                print(letters[:mid])
                print(letters[mid + 1 :])

                print(l, r)
                print(letters[l], letters[r])
                return False
        return True

    def attempt2(self, s: str):  # 7ms 19MB
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
        return self.attempt2(s)
