import collections


class Solution(object):
    def frequencySort(self, s):
        dictionary = sorted(collections.Counter(list(s)).items(), key=lambda x: -x[1])
        return ''.join([(dictionary[i][0] * dictionary[i][1]) for i in range(0, len(dictionary))])


s = Solution()
print(s.frequencySort('tree'))
