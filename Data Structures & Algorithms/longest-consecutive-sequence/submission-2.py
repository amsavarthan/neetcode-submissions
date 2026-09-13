class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        map=set()
        maxL=1

        for num in nums:
            map.add(num)

        arr=[]
        for num in nums:
            if num-1 not in map and num+1 in map:
                arr.append(num)
        
        for n in arr:
            i=n;
            length = 1
            while i+1 in map:
                length+=1
                i+=1
            maxL = max(maxL,length)

        return maxL