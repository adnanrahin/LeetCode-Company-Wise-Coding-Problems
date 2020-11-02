class Solution(object):
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.depthFirstSearch(board, i, j, 0, word):
                        return True

        return False

    def depthFirstSearch(self, board, row, col, counter, word):
        if counter == len(word):
            return True

        if not self.isValid(board, row, col) or word[counter] != board[row][col] or board[row][col] == '.':
            return False

        temp = board[row][col]
        board[row][col] = '.'

        for i in range(len(self.direction)):
            r = self.direction[i][0] + row
            c = self.direction[i][1] + col
            if self.depthFirstSearch(board, r, c, counter + 1, word):
                return True

        board[row][col] = temp

        return False

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def isValid(self, board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])


obj = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(obj.exist(board, word))
