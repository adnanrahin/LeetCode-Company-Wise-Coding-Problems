class Solution(object):
    def lengthOfLongestSubstring(self, s):
        local = 0
        max_len = 0

        dictionary = dict()

        for i in range(0, len(s)):
            if s[i] in dictionary:
                local = max(local, dictionary[s[i]])
            max_len = max(max_len, i + 1 - local)
            dictionary[s[i]] = i + 1

        return max_len
