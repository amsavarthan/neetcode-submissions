class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=i+1
        while i<len(nums) and j<len(nums):
            if(nums[i]+nums[j]==target):
                break;
            j+=1
            if j==len(nums):
                i+=1
                j=i+1

        return [i,j]