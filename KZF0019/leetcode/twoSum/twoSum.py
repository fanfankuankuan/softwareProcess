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
        i = 0
        j = 0
        for z in 4:
            if i < j and nums[i] < nums[j]:
                if nums[i] + nums[j] == target:
                    print i+1
                    print j+1
                    #return i+1,j+1
                    j=0
            else: 
                j=j+1
                print j
                

nu = [1,2,3,4,5]
r = Solution()
read = r.twoSum(nu,4)
