class Solution:

    def try1(self, n):  # O(logN) Hash Table/Simulation | suggestions: O(logN), Floyd's Cycle Finding Algorithm /Simulation
        def reduce(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        seen = set()
        while True:
            n = reduce(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)

    def try2(self, n: int) -> bool:
        def sumOfSquares(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        visit = set()
        while n not in visit:
            n = sumOfSquares(n)
            if n == 1:
                return True
            else:
                visit.add(n)
        return False

    def isHappy(self, n: int) -> bool:  # using floyd's cycle finding algorithm | 1ms 19MB O(log n)
        def getNext(num):
            res = 0
            while num > 0:
                num, rem = divmod(num, 10)
                res += rem**2
            return res

        slow = n
        fast = getNext(n)
        while fast != 1 and fast != slow:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1
