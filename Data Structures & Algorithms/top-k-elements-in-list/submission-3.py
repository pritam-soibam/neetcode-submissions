class Solution:

    def attempt1(self, nums, k):  # 3ms 22MB
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        k_mostfrequent = []
        for num in freq:
            if k == 0:
                break
            k_mostfrequent.append(num[0])
            k -= 1

        return k_mostfrequent

    def attempt2(self, nums, k):  # using hint K is bounded by length of nums
        """
        Current: Hash Table/Bucket Sort
        Suggested: Hash Table/Heap (Priority Queue)/Quickselect
        Key Idea: Count frequencies using a hash map, then use bucket sort to retrieve top k elements in linear time.
        Consider: How would your approach change if the input was a massive data stream instead of a static array?
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucketSort = [[] for _ in range(len(nums))]  # bucketSort.
        for num, count in freq.items():
            i = count - 1
            bucketSort[i].append(num)

        ans = []
        for i in range(len(nums) - 1, -1, -1):
            if k == 0:
                break
            if not bucketSort[i]:
                continue
            ans.extend(bucketSort[i])
            k -= len(bucketSort[i])
        return ans

    def topKFrequent(self, nums: list[int], k: int):
        return self.attempt2(nums, k)