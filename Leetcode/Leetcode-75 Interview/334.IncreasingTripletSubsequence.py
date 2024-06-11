class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #  such that i < j < k and nums[i] < nums[j] < nums[k]

        num_i = num_j = float('inf')
