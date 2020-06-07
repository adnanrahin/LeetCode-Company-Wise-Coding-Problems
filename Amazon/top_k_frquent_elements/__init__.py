import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        dictionary = dict()
        heap = []
        solution = list()

        for i in range(0, len(nums)):
            dictionary[nums[i]] = dictionary.get(nums[i], 0) + 1

        for key, value in dictionary.items():
            temp = (value, key)
            heapq.heappush(heap, temp)

        for i in range(len(heap) - k):
            heapq.heappop(heap)

        for i in range(len(heap)):
            solution.append(heapq.heappop(heap)[1])

        return solution


s = Solution()

data = [1, 1, 1, 2, 2, 3]
freq = 2
print(s.topKFrequent(data, freq))
