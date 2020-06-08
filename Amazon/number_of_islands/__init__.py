class Solution(object):
    direction_array = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def is_valid_move(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def backtrack_(self, grid, row, col):
        if not self.is_valid_move(grid, row, col):
            return
        if grid[row][col] == '0':
            return

        grid[row][col] = '0'
        for i in range(0, len(self.direction_array)):
            self.backtrack_(grid, row + self.direction_array[i][0], col + self.direction_array[i][1])

    def numIslands(self, grid):

        number_of_island = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.backtrack_(grid, i, j)
                    number_of_island += 1

        return number_of_island


s = Solution()
board = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(s.numIslands(board))
