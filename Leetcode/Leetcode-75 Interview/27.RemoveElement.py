class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        numsLen = len(nums)
        k = 0

        for i in range(numsLen):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
