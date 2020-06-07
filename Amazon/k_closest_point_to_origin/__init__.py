from math import sqrt
import heapq


class Solution(object):
    def kClosest(self, points, K):
        k_closest_point = []
        heap = []
        for i in range(0, len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = sqrt(pow(x, 2) + pow(y, 2))
            heapq.heappush(heap, (distance, points[i]))

        for i in range(K):
            k_closest_point.append(heapq.heappop(heap)[1])

        return k_closest_point


s = Solution()

print(s.kClosest([[1, 3], [-2, 2]], 1))
