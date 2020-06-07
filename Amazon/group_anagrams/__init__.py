import collections


class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = collections.defaultdict(list)

        for i in range(0, len(strs)):
            key_string = ''.join(sorted(strs[i]))
            dictionary[key_string].append(strs[i])

        return dictionary.values()


s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
