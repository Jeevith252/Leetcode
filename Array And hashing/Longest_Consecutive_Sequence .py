class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        count , p = 0, 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                p+=1
            else:
                count = max(count,p)
                p=1
        count = max(count,p)
        return count