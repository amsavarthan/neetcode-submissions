class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = -1
        i=len(arr)-1
        while i>=0:
            temp = maxValue
            maxValue = max(arr[i],maxValue)
            arr[i]=temp
            i-=1
        return arr

