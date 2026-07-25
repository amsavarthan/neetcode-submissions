class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=0
        max=n
        for i in range(len(nums)):
            if nums[i] == 1:
                n+=1
            else:
                if n>max:
                    max=n
                n=0
        if n>max:
            max=n
        return max
        