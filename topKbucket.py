from collections import Counter


class Solution:
    def topKBucket(self, nums, k):
        d = Counter(nums)

        # Create a bucket list where freq 0 means no elem occurs, 1 means occurs 1 time...
        bucket = [0] * (len(nums)+1)

        for elem, freq in d.items():
            if bucket[freq] == 0:
                bucket[freq] = [elem]
            else:
                bucket[freq].append(elem)

        # print(bucket)

        result = []
        for i in range(len(bucket), -1, -1):
            if bucket[i-1] != 0:
                result.extend(bucket[i-1])
            if len(result) == k:
                break

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.topKBucket([11, 222, 222, 222, 333, 333, 333, 333], 1)
    print(r)
