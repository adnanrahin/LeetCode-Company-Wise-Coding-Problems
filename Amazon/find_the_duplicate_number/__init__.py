class Solution(object):
    def findDuplicate(self, nums):
        fast_ptr = nums[nums[0]]
        slow_ptr = nums[0]

        while fast_ptr != slow_ptr:
            print(fast_ptr, slow_ptr)
            fast_ptr = nums[nums[fast_ptr]]
            slow_ptr = nums[slow_ptr]

        fast_ptr = 0

        while fast_ptr != slow_ptr:
            fast_ptr = nums[fast_ptr]
            slow_ptr = nums[slow_ptr]

        return fast_ptr


s = Solution()

print(s.findDuplicate([1, 2, 3, 2, 4]))
