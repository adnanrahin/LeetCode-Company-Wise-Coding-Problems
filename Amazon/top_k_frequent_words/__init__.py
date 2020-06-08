import collections


class Solution(object):
    def topKFrequent(self, words, k):
        return [sorted(collections.Counter(words).items(), key=lambda x: (-x[1], x[0]))[i][0] for i in range(k)]


s = Solution()

print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
