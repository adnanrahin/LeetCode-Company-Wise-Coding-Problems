class Solution(object):
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def floodFill(self, image, sr, sc, newColor):

        self.back_track(image, sr, sc, newColor, image[sr][sc])

        return image

    def is_valid(self, image, row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0])

    def back_track(self, image, row, col, new_color, curr_color):

        if not self.is_valid(image, row, col) or image[row][col] == new_color or image[row][col] != curr_color:
            return
        image[row][col] = new_color
        for i in range(len(self.direction)):
            self.back_track(image, self.direction[i][0] + row, self.direction[i][1] + col, new_color, curr_color)

        return


s = Solution()

print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))
