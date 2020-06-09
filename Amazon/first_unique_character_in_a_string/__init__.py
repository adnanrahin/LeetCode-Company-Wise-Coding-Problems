import collections


class Solution(object):
    def firstUniqChar(self, s):
        dictionary = collections.Counter(list(s))
        print(dictionary)
        for i in range(0, len(s)):
            if dictionary[s[i]] == 1:
                return i
        return -1


s = Solution()
print(s.firstUniqChar("sfdfd"))
