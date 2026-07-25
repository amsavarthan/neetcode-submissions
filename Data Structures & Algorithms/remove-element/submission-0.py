class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap=0
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            k+=1
            nums[i],nums[swap]=nums[swap],nums[i]
            swap+=1
        return k
        