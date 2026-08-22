
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        h = []

        for num, freq in count.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)
        return [num for [freq, num] in h]
