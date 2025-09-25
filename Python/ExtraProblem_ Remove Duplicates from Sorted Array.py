# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[a] = nums[i]
                a = a+1
        return a
        