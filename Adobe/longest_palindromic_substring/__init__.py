class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        end = 0
        for i in range(0, len(s)):
            max_len = (max(self.get_longest_palindrome(s, i, i), self.get_longest_palindrome(s, i, i + 1)))
            if max_len > end - start:
                start = i - (int)((max_len - 1) / 2)
                end = i + (int)((max_len) / 2)

        return s[start:end + 1]

    def get_longest_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


s = Solution()
print(s.longestPalindrome("babad"))
