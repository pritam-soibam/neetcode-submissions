class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        k_freq = [[] for _ in range(len(nums))]
        for num, count in freq.items():
            i = count - 1
            k_freq[i].append(num)

        ans = []
        for i in range(len(nums)-1, -1, -1):
            if k == 0: break
            if not k_freq[i]: continue
            ans.extend(k_freq[i])
            k -= len(k_freq[i])
        return ans