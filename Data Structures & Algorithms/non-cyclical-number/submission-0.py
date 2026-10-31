class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def reduce(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        while True:
            n = reduce(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)