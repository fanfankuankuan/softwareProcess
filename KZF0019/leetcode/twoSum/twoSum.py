'''
Created on Jan 10, 2016

@author: KevinFAN
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in len(nums):
            for j in len(nums):
                if i < j and nums[i] < nums[j]:
                    if nums[i] + nums[j] == target:
                        print i+1
                        print j+1
                        #return i+1,j+1

nu = [1,2,3,4]
r = Solution()
read = r.twoSum(nu,4)
