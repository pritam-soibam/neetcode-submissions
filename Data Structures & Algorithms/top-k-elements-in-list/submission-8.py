class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket        
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        bucket = [
            [] for _ in range(len(nums)+1)
        ]
        for num, count in numCount.items():
            bucket[count].append(num)
        

        # top k elements
        res = []
        while bucket:
            nums = bucket.pop()
            for num in nums:
                res.append(num)
                if len(res ) == k:
                    return res

        return res