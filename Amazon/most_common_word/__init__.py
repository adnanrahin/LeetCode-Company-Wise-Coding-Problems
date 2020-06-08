import collections
import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        dictionary = sorted(collections.Counter(re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()).items(),
                            key=lambda x: -x[1])
        banned_vocabulary = set(banned)

        for i in range(0, len(dictionary)):
            if dictionary[i][0] not in banned_vocabulary:
                return dictionary[i][0]


s = Solution()

print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
