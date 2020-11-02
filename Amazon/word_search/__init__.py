class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def isValid(self, board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])


obj = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
