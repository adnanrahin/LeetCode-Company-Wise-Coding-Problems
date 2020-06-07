class Solution(object):

    def twoSum(self, nums, target):
        dictionary = dict()
        for i in range(0, len(nums)):
            dictionary[nums[i]] = i

        for i in range(0, len(nums)):
            sum1 = target - nums[i]
            if sum1 in dictionary and dictionary[sum1] != i:
                return {min(i, dictionary[nums[i]]), max(i, dictionary[nums[i]])}

        return {-1, -1}
