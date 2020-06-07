import heapq


class Solution(object):

    def findKthLargest(self, nums, k):
        pq = []
        for i in range(0, len(nums)):
            heapq.heappush(pq, nums[i])
        for i in range(0, len(nums) - k):
            heapq.heappop(pq)
        return pq[0]


