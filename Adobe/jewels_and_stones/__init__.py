class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels_set = set()
        for i in range(0, len(J)):
            jewels_set.add(J[i])

        number_of_stone = 0

        for i in range(0, len(S)):
            if S[i] in jewels_set:
                number_of_stone += 1

        return number_of_stone
