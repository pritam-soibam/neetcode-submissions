# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]


# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Topic: Array | Hash Table | Divide and Conquer | Sorting | Heap (Priority Queue) | Bucket Sort | Counting | Quickselect


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

    def attempt3(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)

        bucket = [item for nest in bucket for item in nest]
        return bucket[-k:]

    def attempt4(self, nums, k):  # 11ms 24MB
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        while bucket:
            nums = bucket.pop()
            for num in nums:
                result.append(num)
                if len(result) == k:
                    return result
        return result

    def usingBucketSort(self, nums, k):  # idea: using a bucket [[],[],[],..] group the nums based on their frequency as index. finally, pick off the largest Kth elements from the right of bucket.

        # freq -> bucket 0:[], 1;[], ..., n:[]
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in frequency.items():
            print(f"count={count} num={num}")
            bucket[count].append(num)
        print(f"bucket={bucket}")

        # collect Kth largest elements from bucket ... n-1:[] n:[]
        res = []
        while bucket:
            nums = bucket.pop()
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res
        return res

    def topKFrequent(self, nums: list[int], k: int):
        # 1. bucket
        bucket = [[] for _ in range(len(nums)+1)]
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0)+1
        for num, count in numCount.items():
            bucket[count].append(num)

        # 2. top K elements
        res = []
        while bucket:
            nums = bucket.pop()
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res
        return rs