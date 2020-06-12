class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        return sorted([(num1, num2) for num1 in nums1 for num2 in nums2], key=lambda x: (x[1] + x[0]))[:k]


s = Solution()

print(s.kSmallestPairs([1, 2, 4, 5, 6],
                       [3, 5, 7, 9]
                       , 3))
