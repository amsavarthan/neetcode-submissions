class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        flag = False
        for num in nums:
            if num in map:
                flag=True
                break;
            else:
                map[num]=1
        return flag;

        