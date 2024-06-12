class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # init
        n = len(nums)
        not_zero_index = 0

        # nulis non zero dulu
        for i in range(n):
            if nums[i] != 0:
                nums[not_zero_index] = nums[i]
                not_zero_index += 1

        # ngisi yang belakangan-an
        for i in range(not_zero_index, len(nums)):
            nums[i] = 0

        # solution 2 with 2 pointer L R
        # 0 1 2 3
        # L R
        # 1 0 2 3
        #   l R
        # 1 2 0 3
        #     L R
        # 1 2 3 0
        #     L R
        # return 1 2 3 0

        # fix with 2 pointer
        left = 0

        for right in range(n):
            if nums[right] != 0:
                # pertukaran posisi
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
