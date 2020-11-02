class Solution(object):
    def prisonAfterNDays(self, cells, N):
        simulator = set()
        flag = False
        for i in range(0, N):
            new_cells = self.check_for_neighbour(cells)
            pattern = ''.join(map(str, cells))
            if pattern not in simulator:
                simulator.add(pattern)
            elif pattern in simulator:
                flag = True
                break
            cells = new_cells

        if flag is True:
            N = N % len(simulator)
            print(N)
            for i in range(N):
                cells = self.check_for_neighbour(cells)

        return cells

    def check_for_neighbour(self, cells):
        new_cells = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                new_cells[i] = 1
        return new_cells


s = Solution()

print(s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0],
                         1000000000))
