class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Base idea - split by index [s:i + i+1:e] to get the part before and after it
        # calculate the product and store in array.
        # This will be O(n^2) since we multiply after split.

        # lets precalculate prefix and suffix for each index. multiply both to get ans
        # OPTIMAL - use single arr and calc in place

        n = len(nums)
        res = [1]*n

        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix=prefix*nums[i]
    
        suffix = 1
        for i in reversed(range(n)):
            res[i]*=suffix
            suffix=nums[i]*suffix

        return res