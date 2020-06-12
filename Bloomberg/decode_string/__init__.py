class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result_str = ''
        num = 0
        for c in s:
            if c.isalpha():
                result_str += c

            elif c.isnumeric():
                num = 10 * num + int(c)

            elif c == '[':
                stack.append((num, result_str))
                num = 0
                result_str = ''

            else:
                count, old_cur = stack.pop()
                old_cur += (count * result_str)
                result_str = old_cur
        return result_str


s = Solution()
print(s.decodeString('fg2[ac]d'))
