import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        # Create a dictionary of elements and their frequency
        d = Counter(nums)

        # Push tuple of [(frequency, elem)] on min-heap of size k
        # It should be a list because multiple elems can have same freq
        heap = []
        for elem, freq in d.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, elem))
            else:
                _ = heapq.heappushpop(heap, (freq, elem))

        print([h[1] for h in heap])
        return [h[1] for h in heap]


if __name__ == '__main__':
    s = Solution()
    result = s.topKFrequent(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 3], k=2)
    print(result)

