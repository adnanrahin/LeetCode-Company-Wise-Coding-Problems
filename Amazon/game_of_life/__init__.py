class Solution(object):
    directions = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, 0]]

    def gameOfLife(self, board):
        new_board = [([0] * len(board[0])) for i in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                number_of_neighbors = self.count_neighbors(board, row, col)
                if board[row][col] == 1:
                    if number_of_neighbors < 2 or number_of_neighbors > 3:
                        new_board[row][col] = 0
                    elif number_of_neighbors == 2 or number_of_neighbors == 3:
                        new_board[row][col] = 1
                elif board[row][col] == 0:
                    if number_of_neighbors == 3:
                        new_board[row][col] = 1

        for i in range(len(new_board)):
            for j in range(len(new_board[0])):
                board[i][j] = new_board[i][j]

    def count_neighbors(self, board, row, col):
        number_of_neighbors = 0

        for dir in self.directions:
            if self.is_valid_move(board, row + dir[0], col + dir[1]) and board[row + dir[0]][col + dir[1]] == 1:
                number_of_neighbors += 1
        return number_of_neighbors

    def is_valid_move(self, board, row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])


s = Solution()

grid = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

s.gameOfLife(grid)
