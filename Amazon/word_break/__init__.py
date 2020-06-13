class Solution(object):
    def wordBreak(self, s, wordDict):
        vocabulary = set(wordDict)
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(0, len(s) + 1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in vocabulary:
                    dp[i] = True
                    break
        return dp[:-1]


s = Solution()

word = "catsandog"
voca = ["cats", "dog", "sand", "and", "cat"]

print(s.wordBreak(word, voca))
