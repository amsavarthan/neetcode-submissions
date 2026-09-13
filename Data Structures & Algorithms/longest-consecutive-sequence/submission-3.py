class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map=set(nums)
        maxL=0

        for num in nums:
            if num-1 not in map:
                i=num;
                length = 1
                while i+1 in map:
                    length+=1
                    i+=1
                maxL = max(maxL,length)


        return maxL